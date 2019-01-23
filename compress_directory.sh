#!/bin/bash
for filename in ./*; do
	echo $filename
	zip -ur lambda_function_zip.zip $filename
done
