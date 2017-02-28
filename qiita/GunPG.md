# GunPG

    gpgでファイル暗号化
    encrypt files by cmd line.
    
##  パスワードでの暗号化

```
gpg -c <file>
```
### デコード

```
gpg -d <file>
```

[Encrypt with passwd](https://www.cyberciti.biz/tips/linux-how-to-encrypt-and-decrypt-files-with-a-password.html)

## RSAで暗号化する

### RSAでpublicキーprivateキーを生成する

```bash
gpg --gen-key
 # it will show options.
```

生成後 ~/.gunpgにpub, pri キーが保存

```
gpg --encrypt --recipient <USER Name> <file>
#User nameはファイルをデコードしてほしい人をさせている、自分であればgen-keyで使った名前を入力
#これで、.gpgファイルが生成、暗号化されたファイル
 
 
#もしascii形式がほしいであれば
gpg --encrypt --armor --recipient <User name> <file>
```

### デコード
```
gpg <-d|--decrypt> <file>
```

### GunPGサーバからpublicキーをもらう

```
gpg --search-keys --keyserver <server url> 'KEY_ID|E-Mail_ID|REAL_NAME'
```

[More detail](https://www.digitalocean.com/community/tutorials/how-to-use-gpg-to-encrypt-and-sign-messages-on-an-ubuntu-12-04-vps)


