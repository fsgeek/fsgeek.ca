# US Patent 9,830,329 Issued

2017-11-28 · https://fsgeek.ca/log/us-patent-9830329-issued/

US Patent 9,830,329 issued November 28, 2017. It is about a technique for utilizing a pre-existing tunneling mechanism to invoke remote functionality. The original inspiration for this was the need to communicate from a component on a client system to utilize functionality available on the server. The first case for this was when I wanted to obtain meta-data that was maintained on the server, but not available to me on the client. By exploiting a pass-through mechanism in the Windows SMB client, I could send a query to the server, have a component on the server get the answer, and respond back to my software on the client. This turns out to be useful in several cases - and doing it through the existing SMB infrastructure allowed a clean, functional solution.
