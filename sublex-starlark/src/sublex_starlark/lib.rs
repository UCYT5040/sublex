use anyhow::anyhow;
use pyo3::prelude::*;
use starlark::collections::SmallMap;
use starlark::environment::{GlobalsBuilder, Module};
use starlark::eval::Evaluator;
use starlark::syntax::{AstModule, Dialect};
use starlark::values::{Heap, Value};
use starlark::starlark_module;

#[starlark_module]
fn http_module(builder: &mut GlobalsBuilder) {
    fn get<'v>(url: &str, heap: &'v Heap) -> anyhow::Result<Value<'v>> {
        let resp = reqwest::blocking::get(url).map_err(|e| anyhow!(e.to_string()))?;

        let status = resp.status().as_u16() as u32;
        let headers = resp.headers().clone();
        let body = resp.text().map_err(|e| anyhow!(e.to_string()))?;

        let mut headers_map: SmallMap<&str, Value<'v>> = SmallMap::new();
        for (k, v) in headers.iter() {
            headers_map.insert(k.as_str(), heap.alloc(v.to_str().unwrap_or("")));
        }
        let headers_value = heap.alloc(headers_map);

        let mut response_map: SmallMap<&str, Value<'v>> = SmallMap::new();
        response_map.insert("status", heap.alloc(status));
        response_map.insert("body", heap.alloc(body));
        response_map.insert("headers", headers_value);

        Ok(heap.alloc(response_map))
    }
}

#[pyfunction]
fn eval_starlark(script: &str) -> PyResult<String> {
    let dialect = Dialect {
        enable_f_strings: true,
        ..Dialect::Standard
    };
    let ast = AstModule::parse("interactive", script.to_string(), &dialect)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(e.to_string()))?;

    let globals = GlobalsBuilder::new().with(http_module).build();
    let module = Module::new();
    let mut eval = Evaluator::new(&module);

    let result = eval
        .eval_module(ast, &globals)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(e.to_string()))?;

    Ok(result.to_string())
}

#[pymodule]
fn sublex_starlark(_py: Python, m: &Bound<PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(eval_starlark, m)?)?;
    Ok(())
}