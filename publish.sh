#!/bin/bash
#rm index.zip 
#cd lambda 
#zip –r ../index.zip ./
#zip ../index.zip ./*
#cd .. 

# this will upload the zip named : lambda_function_zip.zip that is in the folder
aws lambda create-function --function-name  "new_function2" --runtime "python2.7" --role "arn:aws:iam::785577579649:role/lambda_role_for_rds"  --handler "index.lambda_handler" --zip-file fileb://lambda_function_zip.zip --description "new_test_func" --timeout 2 --region "us-east-1" 

