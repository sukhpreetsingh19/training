REST API : 

Resources : any sort of data available.

1. Uniform Interface: URI (uniform resouce identifier) JSON(popular), XML by using http methods like GET, PUT, POST, DELETE.

2. Client Server Decoupling: Client and server do not know about each other implementation details . they interact only via URI.

3. Statelessnes: Anything required to process a request should be provided with the request itself no data from the previous requests can be used.

4. Cacheability: The server provides the client with the cache information if any. tags [Http Headers]

5. Layered Architecture: varios layers in the system creates a layered architecture eg Network Layer and Aplication layer.

6. Code on Demand(optional): We supply the client with code over network in some usable format.