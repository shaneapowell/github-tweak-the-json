# github-tweak-the-json


A simple github action to read or write or update a local json file.

I created this because so many other actions out there rely on the runner being setup with Node.  We use a number of self-hosted runners that do not have node setup.  

Not dependant on python being installed on your runner since this runs inside it's own python image, so should work on self-hosted as well as cloud runners.

# Syntax
```yaml
- uses: shaneapowell/github-tweak-the-json@v1
  with: 
    action: [write/read]
    filename: <filename>
    field: <json field path>
    value: <some value>
```
- `action` Must be either `write` or `read`.  When in `read` mode, the value is returned through the output name `value`
- `filename` Simply the file name to read or write.
- `field` The dot-notation json field.  Arrays are not currently supported.
  - `user`  == { 'user': 'john' }
  - `user.firstname` == { 'user': { 'firstname': 'john' } }
- `value` The value to write. Ignored when in `read` mode.

# Usage Examples
see [action.yml](action.yml)

**Write the github run number to the manifest.json file**
```yaml
- uses: shaneapowell/github-tweak-the-json@v1
  with: 
    action: write
    filename: manifest.json
    field: buildNumber
    value: "${{ github.run_number }}"   
```

**Write a value to a nested json field**
```yaml
- uses: shaneapowell/github-tweak-the-json@v1
  with: 
    action: write
    filename: userdata.json
    field: user.email.label
    value: GMail
```

**Read a value**
```yaml
- uses: shaneapowell/github-tweak-the-json@v1
  id: jsonread
  with: 
    action: read
    filename: manifest.json
    field: version
    
- run: echo "${{ steps.jsonread.outputs.value }}"
```


# License
The scripts and documentaiton in this project are released under the [MIT License](LICENSE)