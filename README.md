# Licence Plate Recognition

LPR (Licence Plate Recognition) implemented by serverless, and serverful for comparison.


- `serverless` directory contains the serverless implementation
- `serverful` directory contains the serverful implementation

## Serverless Solution
Based on [Alibaba Cloud Serverless Function Computing](https://www.aliyun.com/product/fc)

Serverless Workflow:

1. Write business logic code
2. Write trigger code
3. Deploy


## Serverful Solution

Serverful Workflow:

1. Write business logic code
2. Write HTTP handler code
3. Write Dockerfile
4. Write Makefile
5. Connect to remote server for setting up environment
6. Deploy


## Usage
- Request `GET /lpr?image={image_base64}` to execute lpr

- Request `GET /test` to test lpr result