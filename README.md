# Azure Cloud-Based Data Lake System With Azure CLI and Python

## Project Overview

A fintech organization, is on a mission to decentralize financial services globally. The goal is to build a cloud-based data lake system on Azure. This system will ingest both structured and unstructured data for analytics using Spark. This project involves choosing the appropriate Azure storage solution, setting up the necessary infrastructure, and automating data ingestion.

## Storage Solution Choice

### Azure ADLS Gen2 vs. ADLS Gen1

**Chosen Storage Solution**: Azure Data Lake Storage Gen2

**Justification**:
- **Performance**: ADLS Gen2 offers better performance for analytics workloads due to its integration with Azure Blob Storage.
- **Cost Efficiency**: Gen2 provides more cost-effective storage and access options, which is crucial for managing large datasets.
- **Security**: It includes enhanced security features such as fine-grained access controls with Azure Active Directory (AAD) integration.
- **Integration**: Gen2 is well-integrated with Azure's ecosystem, making it ideal for analytics with Azure Databricks and Spark.

### Replication Type

**Chosen Replication Set**: Geo-redundant storage (GRS)

**Justification**:
- **Business Continuity**: GRS ensures data availability and durability by replicating data to a secondary region, which is essential for a global fintech organization like Kowope.
- **Disaster Recovery**: Provides strong disaster recovery capabilities, minimizing data loss risks in case of regional outages.

### Storage Account Tier

**Chosen Tier**: Hot Tier

**Justification**:
- **Frequent Access**: The hot tier is ideal for data that needs to be accessed frequently, such as data being processed for analytics.
- **Cost-Effective**: While more expensive for storage, the hot tier reduces costs for frequent access patterns, aligning with the project's data usage needs.

## Project Details

The project involves the following steps:

1. **Set Up Azure Resources**: 
   - Use Azure CLI to:
   - Create a resource group.
   - Create a storage account with hierarchical namespace enabled.
   - Create a file system (container) in the storage account.

2. **Upload Files**: 
    - Use Python to  upload files to the Azure Data Lake Storage Gen2.

3. **Tools Used**:
   - Azure CLI
   - Python