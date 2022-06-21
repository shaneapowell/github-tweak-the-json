# github-tweak-the-json - JSON read/write utility.
What makes this one a little different is that is uses it's own Docker Container to run the command.  Does not rely on the running host.

Many utility actions available expect your job to be run directly on one of GitHubs `ubuntu-latest` runners.  These utilities often use `nodejs` to run a simple script.  This expects `nodejs` to be available directly with the given action job you are running.  But if you use a specific docker image to run your job from a specific container (eg, python:3.8-slim, or alpine), the `nodejs` binary will not be available to the action.

This action uses a very basic Dockerfile to specify the image to run it.  Nothing more than an alpine image with nodejs installed.  As a result, this action should run just fine on any workflow/job/container combination you can create.

I created this because so many other actions out there rely on the runner being setup with Node.  We use a number of self-hosted runners that do not have node setup.  

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
  - `user` --> { 'user': 'john' }
  - `user.firstname` --> { 'user': { 'firstname': 'john' } }
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
