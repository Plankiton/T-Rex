# Translater

If you did have problems with text conversion, this ultil is the solution, maked for anyperson and easy to learn, you just have to make a configuration file with the patterns of the languages and the translater will translate.

# How its works

You have to make a file with the extension ".yml" or ".yaml" and write the `pattern` and the `replace` (`<pattern>: <replace>`):

```YAML
foo: bar
```

> When the translate find the word "pattern" will translate to "replace".

In the `pattern` you can use regular exprections like:

```YAML
"^word \-\> (foo|bar)": "foobar is a stranger word!"
```

> But never use regular exprections in the `replace` or the translater will replace the especial symbols.

But this is easy to the translater, you can to use the variables for get informations of the text:

```YAML
"^word \-\> %foobar&": "%foobar& is a stranger word!"
```

> When the translater find `%foobar&` in `replace` will replace to the text in `pattern`, so, "word -> joao" would be replaced to "joao is a stranger word!"
