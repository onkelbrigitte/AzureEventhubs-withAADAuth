# Azure Eventhubs with AAD authentication.
[Azure Event Hubs](https://docs.microsoft.com/en-us/azure/event-hubs/) allows for several authentication methods such as SAS tokens and pre-shared keys. However, additionally, Azure Active Directory (AAD) is supported. This is considered the best choice from a security perspective as it allows several methods such as certificate based authentification. 

I couldn't find good examples how to use it for the authentication scenarios that I am interested in, so I created this samples.

First sample is for simple SPNs secrets for an AAD service principle that has access to a given Eventhub. The second sample uses a certificate. 

I am using the Azure Eventhub SDK and the Azure MSAL library. Both have to be installed in order to run the script.