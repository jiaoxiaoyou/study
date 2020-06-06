#!/usr/bin/env bash

ADDRESS=$1

if [ -z $ADDRESS ]; then
  ADDRESS="localhost:9200"
fi

# Check that Elasticsearch is running
curl -s "http://$ADDRESS" 2>&1 > /dev/null
if [ $? != 0 ]; then
    echo "Unable to contact Elasticsearch at $ADDRESS"
    echo "Please ensure Elasticsearch is running and can be reached at http://$ADDRESS/"
    exit -1
fi

echo "WARNING, this script will delete the 'good' and the 'myindex' indices and re-index all data!"
echo "Press Control-C to cancel this operation."
echo
echo "Press [Enter] to continue."
read

# Delete the old index, swallow failures if it doesn't exist
curl -s -XDELETE "$ADDRESS/goods" > /dev/null

# Create the next index using mapping.json
#echo "Creating 'good' index..."
#curl -s -XPUT -H'Content-Type: application/json' "$ADDRESS/goods" -d@$(dirname $0)/mapping.json

# Wait for index to become yellow
curl -s "$ADDRESS/goods/_health?wait_for_status=yellow&timeout=10s" > /dev/null
echo
echo "Done creating 'goods' index."

echo
echo "Indexing data..."

echo "Indexing groups..."
curl -s -XPOST "$ADDRESS/goods/fruit/1" -H'Content-Type: application/json' -d'{
	"name": "xiangjiao",
    "price": 60,
    "producer": "zhongguo",
    "desc": "xiangtian,kekou",
    "tags": [
        "chang",
        "zhi",
        "huang"
    ]
}'

echo
curl -s -XPOST "$ADDRESS/goods/fruit/2" -H'Content-Type: application/json' -d'{
    "name": "pingguo",
    "price": 20,
    "producer": "zhongguo",
    "desc": "haixing,haochi",
    "tags": [
        "da",
        "yuan"
    ]
}'

echo
curl -s -XPOST "$ADDRESS/goods/fruit/3" -H'Content-Type: application/json' -d'{
	"name": "lzi",
    "price": 10,
    "producer": "zhongguo",
    "desc": "zide",
    "tags": [
        "suan",
        "tian"
    ]
}'

echo
curl -s -XPOST "$ADDRESS/goods/fruit/4" -H'Content-Type: application/json' -d'{
    "name": "boluo",
    "price": 74,
    "producer": "zhongguo",
    "desc": "getouda",
    "tags": [
        "huang",
        "youci"
    ]
}'

echo
curl -s -XPOST "$ADDRESS/goods/fruit/5" -H'Content-Type: application/json' -d'{
    "name": "mihoutao",
    "price": 45,
    "producer": "xinxilan",
    "desc": "suan",
    "tags": [
        "lv",
        "huang"
    ]
}'

echo
curl -s -XPOST "$ADDRESS/goods/fruit/6" -H'Content-Type: application/json' -d'{
    "name": "xigua",
    "price": 109,
    "producer": "zhongguo",
    "desc": "haochi",
    "tags": [
        "da",
        "haochi"
    ]
}'

echo
curl -s -XPOST "$ADDRESS/goods/fruit/7" -H'Content-Type: application/json' -d'{
    "name": "pingguo",
    "price": 109,
    "producer": "zhongguo",
    "desc": "haochi",
    "tags": [
        "da",
        "haochi"
    ]
}'

echo
curl -s -XPOST "$ADDRESS/goods/fruit/8" -H'Content-Type: application/json' -d'{
    "name": "pingguo",
	"price": 120,
	"producer": "USA",
	"desc": "haochi",
	"tags": [
	"da",
	"haochi"
	]
}'

echo
curl -s -XPOST "$ADDRESS/goods/fruit/9" -H'Content-Type: application/json' -d'{
    "name": "pingguo",
	"price": 220,
	"producer": "USA",
	"desc": "haochi",
	"tags": [
	"da",
	"haochi"
	]
}'

echo
echo "Done indexing groups."


echo
