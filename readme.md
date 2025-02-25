┌───────────────────────────────┐
│          User's Browser       │
└───────────────┬───────────────┘
                │ (HTTP Requests/Responses)
                ▼
┌───────────────────────────────┐
│          Web Server           │
│ (e.g., Nginx/Apache/Gunicorn) │
└───────────────┬───────────────┘
                │ (Proxy to Django App)
                ▼
┌───────────────────────────────┐
│        Django Application     │
├───────────────────────────────┤
│ ┌──────────┐  ┌───────────┐   │
│ │   URLs   │  │  Settings │   │
│ └────┬─────┘  └─────┬─────┘   │
│      │              │         │
│      ▼              │         │
│ ┌──────────┐        │         │
│ │  Views   │◄───────┘         │
│ └────┬─────┘                  │
│      │                        │
│      ├───────────────────────►│
│      │  ┌──────────┐  ┌─────┐ │
│      │  │  Forms   │  │ Auth│ │
│      │  └────────┬─┘  └──┬──┘ │
│      ▼           ▼       ▼    │
│ ┌──────────┐  ┌──────────┐    │
│ │ Templates│  │  Models  │    │
│ └────┬─────┘  └────┬─────┘    │
│      │              │         │
│      │              ▼         │
│      │  ┌───────────────────┐ │
│      │  │   Database (ORM)  │ │
│      │  │ (PostgreSQL/MySQL)│ │
│      │  └──────────┬────────┘ │
│      │             │          │
│      ▼             ▼          │
│ ┌───────────────────────────┐ │
│ │ Static/Media Files (S3)   │ │
│ └───────────────────────────┘ │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│    External Services/APIs     │
│ (Email, Payment Gateways, etc)│
└───────────────────────────────┘