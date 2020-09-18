# BrandTag Integration Examples

For QR code verify redirect, look at `/redirect.html`

For landing page certificate payload look at `/certificate.html`

## To Run

1. Install python3

2. Run
```
python server.py
```

## Sample QR Redirect
```
# Valid Redirect
localhost:8000/v/3bcCCfdY to test sample code
```

## Sample Certificate Data Fetch

```
# Valid Activated
localhost:8000/certificate?m=luxtag_sdn_bhd&a=SDSNU67XJ3UA5IEPYJKYMRGJQJLV3HIZZ23SRL4N

# Valid Not Activated
localhost:8000/certificate?m=jt-enterprise&a=SDVDZNXICWVWWZJ2XNLBN7QINLXFCFAPS4HWGWYF
```
