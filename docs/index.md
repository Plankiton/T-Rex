# TextAnalizer

The TextAnalizer is a simple ultility for text analitics, your especiality is translate some text to other text.

## Install

Verify if you `$PATH` variable has the directory `$HOME/.local/bin`, why is the local where the `pip` will save the executable files, if not take a next command and reload your desktop session to load the setting.

> I'm not talking to you reboot your machine, just logout and login again.

```sh
$ echo 'export PATH="$PATH:$HOME/.local/bin"' >> .xprofile
```

And is just run the next command and done!

```sh
$ pip install git+http://github.com/RoboCopGay/TextAnalizer --user && getter -h > /dev/null && if [[ "$?"==0 ]];then echo 'TextAnalizer are installed!!';fi
```

# Getting started

## Using "translater" tool

Changing `"foo" to "bar"` on the text `"foo is bar"`:

```sh
$ echo "foo bar"| translater 'foo: bar'

bar bar
```
> The space(' ') after the ':' token is needed on `pattern` of translater.

Or changing word before `bar` to `foo`:

```sh
$ echo "thingbar, somethingbar" | translater "'\\w{1,}bar': foobar"
```

> The `\\` is needed because of quote dont accept the `\`.

Or changing `"foo<complement>"` to `"<complement>bar"`.

```sh
$ echo "foosomething"| translater '"foo%complement&": "%complement&bar"'

somethingbar
```

With the `translater` you too can search in a file, is just use the `-f <file>`:

> file.txt

```
name Jack
old 23
```

```sh
$ translater -f file.txt '"%key& %value&": "the %key& has the %value& value."'

the name has the Jack value.
the old has the 23 value.
```

And you too can use a file as `pattern` using the `-c` opition:

> file.txt

```
hi, I am Brazilian.
```

> conf.yml

```yaml
hi: Oi
I: eu
am: sou
Brazilian: Brasileiro
```

```sh
$ translater -f file.txt -c conf.yml

Oi, eu sou Brasileiro.
```

## Using "getter" tool
