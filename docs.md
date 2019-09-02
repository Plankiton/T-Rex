# Get Started

You have to make a file with the extension ".yml" or ".yaml" and write the `pattern` and the `replace` (`<pattern>: <replace>`):

```YAML
foo: bar
```

> When the translater find the word "foo" will translate to "bar".

In the `pattern` you can use regular expressions like:

```YAML
'^word \-\> (foo|bar)': "foobar is a stranger word!"
```

> But never use regular expressions in the `replace`.

You can too to use the variables for get informations of the text:

```YAML
'^word \-\> %foobar&': "%foobar& is a stranger word!"
```

> When the translater find `%foobar&` in `replace` will replace by the text in `pattern`, so, the text "word -> joao" would be replaced by "joao is a stranger word!"

# Evals

Evals are parts of code writed in python that will be executed in your key:

```YAML
"five joao": ' !{ 5*"joao" } '
```

> The command in between `!{` and `}` will be executed by python and the result will be "joaojoaojoaojoaojoao"

But evals only can be used in `replace`, therefore the next example do not will be executed:

```YAML
"!{ "\tfive joao \n ".strip() }": ' "joaojoaojoaojoaojoao" '
```

# Especial keys

In the config file exists any especial keys for the most varied functions, each one with your peculiarity.

As the `key` ( or `pattern` ) and `replace` already seen in begin, they will be jumped.

## Name and key

When we declare one `element`, they can have a name for we to mention him, and exists 2 forms of do this.

The first one is like this:

```YAML
'^foo\ {0,}':
   name: 'foo'
   replace: 'bar'


<pattern>:
   name: <name>
   replace: <replace>
```

And the second is like this:

```YAML
foo:
   pattern: '^foo\ {0,}'
   replace: 'bar'


<name>:
   pattern: <pattern>
   replace: <replace>
```

By default, the `pattern` is refered as "name" of the `element`, but if exists the key `pattern` in this `element`, so "name" will be `name`.

And the general form is:

```YAML
<name of element>:
   pattern: <pattern>
   name: <name>
   replace: <replace>
```

> Remember that `name of element`, can take over the form of `pattern` or `name` if not refered, and by default is `pattern`

