# Object-Oriented Programming

OOP and low-level design practice from my local Interview Room application.

## Automatic synchronization

- **Interviews:** finishing a session uploads the final source code to `<problem>/session-<id>.<extension>`.
- **OOP laboratory:** a successful execution uploads the source code to `laboratory/<language>/submission-<fingerprint>.<extension>`.
- Syntax checks, compilation without execution, and failed executions do not upload laboratory submissions.
- Identical laboratory code is uploaded once. Different versions are kept as separate submissions.

Only source code is synchronized. Interview notes, statements, access links, credentials, and local databases stay on the local computer.

Pending uploads are saved locally and retried every minute while the application is running, including after a restart. The application displays a link when an upload completes.

Languages: Python, JavaScript, Java, and C++.
