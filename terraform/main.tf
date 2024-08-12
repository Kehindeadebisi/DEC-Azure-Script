resource "azurerm_resource_group" "kowoperg" {
  name     = "kowope -rg"
  location = "West Europe"
}

resource "azurerm_storage_account" "kowopesta" {
  name                     = "kowopesta"
  resource_group_name      = azurerm_resource_group.kowoperg.name
  location                 = azurerm_resource_group.kowoperg.location
  account_tier             = "Standard"
  account_replication_type = "GRS"

  tags = {
    environment = "staging"
  }
}