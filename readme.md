# TextAnalizer

![TextAnalizer banner](assets/icon.light.png)

The TextAnalizer is a simple ultility for text analitics, your especiality is translate some text to other text.

> Using "translater" tool

Changing "foo" to "bar" on the text "foo bar":

```sh
$ echo "foo bar"| translater 'foo: bar'

bar bar
```
> The space(' ') after the ':' token is needed on translater.

Or changing "foo%complement&" to "%complement&bar"

```sh
$ echo "foosomething"| translater '"foo%complement&": "%complement&bar"'

somethingbar
```

> Using "getter" tool

Or if you want search emails on any text using a regex ".{1,}@.{1,}":

```sh
$ echo "j@gmail.com
person@site.net
some text to try confuse the getter
email@g.com" | getter ".{1,}@.{1,}"

j@gmail.com
person@site.net
email@g.com
```

Or getting just the username of emails:

```sh
$ echo "j@gmail.com
person@site.net
some text to try confuse the getter
email@g.com" | getter "%username:.{1,}&@.{1,}" -t "%username&"

j
person
email
```

## Install

To install the textanalizer is just take this in a terminal:

```sh
$ pip install git+http://github.com/RoboCopGay/TextAnalizer --user && getter -h > /dev/null && if [[ "$?"==0 ]];then echo 'TextAnalizer are installed!!';fi
```

# Documentation

If your want learn more about the TextAnalizer is just enter on [AnaLixerDocs](http://robocopgay.github.io/TextAnalizer).
