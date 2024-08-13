resource "azurerm_resource_group" "kowoperg" {
  name     = "kowoperg"
  location = "westus"
}

resource "azurerm_storage_account" "kowopesta" {
  name                     = "kowopesta"
  resource_group_name      = azurerm_resource_group.kowoperg.name
  location                 = azurerm_resource_group.kowoperg.location
  account_tier             = "Standard"
  account_replication_type = "GRS"
  is_hns_enabled = true
  account_kind = "StorageV2"

  tags = {
    environment = "staging"
  }
}