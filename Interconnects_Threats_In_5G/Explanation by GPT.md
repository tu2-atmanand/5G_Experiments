
### **What is HTTP/2 used in 5G Core**

HTTP/2 is not explicitly used in the 5G architecture itself; instead, it is often employed in the context of web-based services and applications that interact with the 5G Core (5GC) network. The 5G architecture, defined by standards like 3GPP (Third Generation Partnership Project), primarily focuses on the radio and core network aspects to enable advanced mobile communication. However, when it comes to providing services to end-users or connecting with external systems, HTTP/2 may be utilized.

Here's an overview of HTTP/2 and its potential use in the context of 5G:

1. **HTTP/2 Overview:**
   - **Multiplexing:** One of the key features of HTTP/2 is multiplexing, which allows multiple requests and responses to be sent in parallel over a single connection. This is particularly beneficial for reducing latency and improving the efficiency of data transfer.

   - **Header Compression:** HTTP/2 uses header compression, which minimizes the overhead associated with sending headers with each request and response. This leads to reduced bandwidth usage and faster data transfer.

   - **Binary Protocol:** Unlike its predecessor HTTP/1.x, which uses a text-based protocol, HTTP/2 is a binary protocol. This facilitates more efficient parsing and reduces errors in data transmission.

   - **Server Push:** HTTP/2 introduces server push, enabling servers to send additional resources (e.g., images, stylesheets) to the client before the client explicitly requests them. This can enhance the loading speed of web pages.

2. **Use in 5G Services:**
   - **Enhanced Mobile Broadband (eMBB):** HTTP/2 can be employed to optimize the delivery of web content, such as streaming videos, images, and other media, for enhanced mobile broadband services in 5G networks.

   - **Low Latency Communications (URLLC):** The multiplexing feature of HTTP/2 is particularly beneficial for low-latency applications, such as real-time communication and gaming, which are part of the Ultra-Reliable Low Latency Communications (URLLC) use case in 5G.

   - **Massive Machine Type Communications (mMTC):** In scenarios involving massive machine-type communications, HTTP/2 can be utilized for efficient data exchange between devices and servers.

3. **Integration with APIs and Web Services:**
   - HTTP/2 is commonly used in modern web services and APIs. 5G networks may leverage these APIs for various services, including IoT (Internet of Things) communication, content delivery, and application interactions.

4. **Security Considerations:**
   - When HTTP/2 is employed, it is recommended to use it over a secure connection (HTTPS). This ensures data integrity and confidentiality, which is crucial for secure communication in 5G networks.

In summary, while HTTP/2 itself is not a fundamental part of the 5G architecture, its features make it a suitable choice for optimizing data transfer and improving the performance of web-based services and applications that interact with the 5G Core. Its use is more prevalent in the application layer, complementing the capabilities of the 5G network.


### Threats associated with 5G Core network

Security is a critical concern in any network, including 5G, where the use of HTTP-based protocols introduces potential vulnerabilities. Here are some considerations regarding security threats associated with HTTP in the context of 5G Core (5GC) components like AMF (Access and Mobility Management Function) and SMF (Session Management Function):

1. **Man-in-the-Middle (MitM) Attacks:**
   - **Description:** A Man-in-the-Middle attacker intercepts communication between network components, potentially gaining unauthorized access to sensitive information.
   - **Mitigation:** To prevent MitM attacks, it's crucial to implement secure communication channels. This often involves using HTTPS instead of HTTP, ensuring that data is encrypted during transit. Additionally, strong authentication mechanisms, such as mutual TLS (Transport Layer Security) authentication, can be employed.

2. **Data Tampering:**
   - **Description:** Attackers may attempt to tamper with the data being exchanged between components, leading to unauthorized modifications or injections of malicious content.
   - **Mitigation:** Implementing message integrity checks, such as digital signatures or Message Authentication Codes (MACs), can ensure that the received data has not been altered during transit. Additionally, using secure channels like HTTPS helps prevent data tampering.

3. **Unauthorized Access and Information Disclosure:**
   - **Description:** If an attacker gains unauthorized access to the 5G Core or specific components like AMF and SMF, they may retrieve sensitive user information or manipulate network operations.
   - **Mitigation:** Implement strict access controls, strong authentication mechanisms, and encryption for both intra-network and inter-network communications. Regular security audits and monitoring can help detect and mitigate unauthorized access.

4. **Denial-of-Service (DoS) Attacks:**
   - **Description:** DoS attacks aim to disrupt the normal functioning of network components by overwhelming them with a high volume of requests, leading to service degradation or unavailability.
   - **Mitigation:** Employ traffic filtering, rate limiting, and intrusion detection/prevention systems to identify and mitigate potential DoS attacks. Additionally, implementing load balancing can distribute incoming requests evenly across multiple servers, enhancing resilience.

5. **Session Hijacking:**
   - **Description:** Attackers may attempt to hijack user sessions, gaining unauthorized access to ongoing communication sessions between devices and network components.
   - **Mitigation:** Use secure session management practices, such as session tokens with short lifetimes, and regularly rotate session keys. Implement mechanisms like session encryption to protect session data from being intercepted.

6. **Security in API Communications:**
   - **Description:** Many 5G services rely on APIs for communication between components. Insecure API implementations can lead to data exposure, unauthorized access, and injection attacks.
   - **Mitigation:** Implement secure coding practices for API development, use OAuth or other secure authentication mechanisms, validate and sanitize input data, and regularly update API security configurations.

In conclusion, securing HTTP-based communication in 5G networks involves a combination of encryption, authentication, access controls, and monitoring mechanisms. Implementing security best practices at both the transport layer (e.g., HTTPS) and application layer (e.g., secure APIs) is essential to mitigate potential threats and vulnerabilities. Regular security assessments and updates are crucial to adapt to evolving security challenges.