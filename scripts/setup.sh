#!/bin/bash

RESOURCE_GROUP_NAME="kowoperg"
LOCATION="westus"
STORAGE_ACCOUNT_NAME="kowopesta"
SKU="Standard_GRS"

echo "Creating resource group..."
az group create --name $RESOURCE_GROUP_NAME --location $LOCATION 

RESOURCE_GROUP_EXISTS=$(az group exists --name $RESOURCE_GROUP_NAME)

if [ "$RESOURCE_GROUP_EXISTS" = true ]; then
    echo "Resource group '$RESOURCE_GROUP_NAME' created successfully."
else
    echo "Failed to create resource group '$RESOURCE_GROUP_NAME'. Exiting."
    exit 1

echo "Checking if storage account name '$STORAGE_ACCOUNT_NAME' is available..."
STORAGE_ACCOUNT_AVAILABLE=$(az storage account check-name --name $STORAGE_ACCOUNT_NAME --query "nameAvailable" -o tsv)

if [ "$STORAGE_ACCOUNT_AVAILABLE" = false ]; then
    echo "Storage account name '$STORAGE_ACCOUNT_NAME' is already in use."
    exit 1

echo "Creating storage account..."
az storage account create \
    --name $STORAGE_ACCOUNT_NAME \
    --resource-group $RESOURCE_GROUP_NAME \
    --location $LOCATION \
    --sku $SKU \
    --kind StorageV2 \
    --hierarchical-namespace true

STORAGE_ACCOUNT_CREATION_STATUS=$(az storage account show --name $STORAGE_ACCOUNT_NAME --resource-group $RESOURCE_GROUP_NAME --query "provisioningState" -o tsv)

if [ "$STORAGE_ACCOUNT_CREATION_STATUS" = "Succeeded" ]; then
    echo "Storage account '$STORAGE_ACCOUNT_NAME' created successfully."
else
    echo "Failed to create storage account '$STORAGE_ACCOUNT_NAME'"
    exit 1

