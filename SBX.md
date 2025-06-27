# Writing SBXs (search configurations)

## Format

SBXs use Lua to define and execute start configurations. You can configure your editor to treat `.sbx` files as Lua files for syntax highlighting and linting.

## Header

Your SBX file must begin with a `sublex_data` header:

```lua
sublex_data = {
    name = "Poetry",
    description = "Search for poetry.",
    version = "1.0.0",
    author = "Sublex",
    tags = {"poetry", "literature", "poem", "poems", "poet"},
    supported_filters = {
        query = {"search", "title"},
        author = {"poet"}
    },
    permissions = {
        network = {
            targets = { -- List of domains/IPs that the SBX can access
                "poetrydb.org"
            }
        }
    }
}
```

### Permissions

Permissions are not yet implemented. In the future, you may need to update your SBX to request permissions for certain actions that will be restricted.

For now, include permissions for HTTP requests, although this is not yet enforced.

## Functions

You should implement a `sublex_execute` function:

```lua
function sublex_execute(interface, filters)
```

### Interface

This provides access to some useful functions. See `sublex/sbx/execute/interface` for the full list of available functions.

### Filters

This is a table containing the filters that the user has applied. Note that aliases are handled automatically, so you only need to handle the canonical names.