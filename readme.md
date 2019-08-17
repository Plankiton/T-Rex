# Translater

If you did have problems with text conversion, this ultil is the solution, maked for anyperson and easy to learn, you just have to make a configuration file with the patterns of the languages and the translater will translate.

# How its works

You have to make a file with the extension ".yml" or ".yaml" and write the `pattern` and the `replace` (`<pattern>: <replace>`):

```YAML
foo: bar
```

> When the translater find the word "foo" will translate to "bar".

In the `pattern` you can use regular expressions like:

```YAML
"^word \-\> (foo|bar)": "foobar is a stranger word!"
```

> But never use regular expressions in the `replace`.

You can too to use the variables for get informations of the text:

```YAML
"^word \-\> %foobar&": "%foobar& is a stranger word!"
```

> When the translater find `%foobar&` in `replace` will replace by the text in `pattern`, so, "word -> joao" would be replaced by "joao is a stranger word!"
