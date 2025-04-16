<!--
 * @Author: Vincent Young
 * @Date: 2022-11-17 02:07:33
 * @LastEditors: Vincent Young
 * @LastEditTime: 2022-11-17 03:33:16
 * @FilePath: /ASN-China/README.md
 * @Telegram: https://t.me/missuo
 * 
 * Copyright © 2022 by Vincent, All Rights Reserved. 
-->
# ASN-China
ASN and IP list in China library.

## Features
- Automatic daily updates
- Reliable and accurate source
- Including overseas business of Chinese companies
## Use in proxy app
### Surge
```
[Rule]
# > China ASN IP List
RULE-SET, https://cdn.jsdelivr.net/gh/vialib/ASN-China@main/IP.ASN.China.txt, Direct
```

### Clash
```
rule-providers:
  asn-cn:
    type: http
    behavior: ipcidr
    url: https://cdn.jsdelivr.net/gh/vialib/ASN-China@main/IP.ASN.China.yaml
    path: "./rule_provider/IP.ASN.China.yaml"
    interval: 86400

rules:
    - RULE-SET,asn-cn,DIRECT
```


## Data Source
### ASN Information
- [bgp.he.net](https://bgp.he.net/country/CN)

### IP Information
- [cbuijs/ipasn](https://github.com/cbuijs/ipasn)

### ASN-IP Information
- [ipverse/asn-ip](https://github.com/ipverse/asn-ip)

## Author's ASN
**[AS206729](https://bgp.he.net/AS206729)**

The ASN name has been officially changed in the Jan 20, 2022 UTC [Commit](https://github.com/missuo/ASN-China/commit/4345acd8e146c99d56792977d88ed1d6417c9e22).

## Author

**ASN-China** © [Vincent Young](https://github.com/missuo), Released under the [MIT](./LICENSE) License.<br>


