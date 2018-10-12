
### About

simple tfvars (HCL) converter

### Usage

```
usage: json2tfvars [-h] [--reverse] [--indent N] [FILE [FILE ...]]

positional arguments:
  FILE

optional arguments:
  -h, --help  show this help message and exit
  --reverse   expect tfvars (HCL) input
  --indent N  adjust identation levels
```

```bash
$ json2tfvars <<< '{"a":"b"}' | json2tfvars --reverse | jq -r '. + {"c":"d"}' | json2tfvars

a = "b"

c = "d"

```

[//]: # ( vim:set ts=2 sw=2 et syn=markdown: )
