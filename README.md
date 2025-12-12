# OpsIQ

OpsIQ is a SaaS platform built with a modular monolith architecture following hexagonal (Ports & Adapters) principles.

## Architecture

- **Backend**: Python 3.13 + FastAPI with hexagonal architecture
- **Frontend**: TypeScript + Next.js 16 App Router
- **Data Plane**: Databricks (stubbed for development)
- **Architecture Style**: Hexagonal (domain / ports / adapters / api)

## Project Structure

```
opsiq/
├── backend/              # FastAPI backend
│   ├── engines/         # Business logic engines
│   │   └── retention/   # Trip Frequency & Retention Engine
│   ├── platform_core/   # Core platform components (tenants, etc.)
│   ├── shared/          # Shared infrastructure
│   └── tests/           # Test suite
├── frontend/            # Next.js frontend
│   └── app/            # Next.js App Router pages
└── docker-compose.yml   # Development environment
```

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.13 (for local development)
- Node.js 23+ (for local development)

### Running with Docker

1. Clone the repository:
```bash
git clone <repository-url>
cd opsiq
```

2. Start the services:
```bash
docker-compose up
```

3. Access the application:
   - Backend API: http://localhost:8000
   - Frontend: http://localhost:3000
   - Health check: http://localhost:8000/health
   - Retention API: http://localhost:8000/tenants/demo/retention/summary
   - Retention UI: http://localhost:3000/tenants/demo/retention

### Local Development

#### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

#### Frontend

```bash
cd frontend
yarn install
yarn dev
```

## Testing

### Backend Tests

```bash
cd backend
pytest
```

With coverage:
```bash
pytest --cov=engines/retention/domain --cov-report=html
```

### Frontend Tests

```bash
cd frontend
yarn test
```

## API Endpoints

### Health Check
- `GET /health` - Health check endpoint

### Retention Engine
- `GET /tenants/{tenant_id}/retention/summary` - Get retention summary for a tenant

## Development

### Architecture Principles

1. **Domain Layer**: Pure business logic with no infrastructure dependencies
2. **Ports**: Abstract interfaces (ABCs) only
3. **Adapters**: Infrastructure implementations and composition
4. **API Layer**: FastAPI routers only

### Adding a New Engine

1. Create engine directory under `backend/engines/`
2. Follow the structure: `domain/`, `ports/`, `adapters/`, `api/`
3. Wire the router in `backend/main.py`

## CI/CD

The project includes GitHub Actions workflows for:
- Backend: pytest, ruff linting, coverage
- Frontend: build verification

See `.github/workflows/ci.yml` for details.

## License

[Add your license here]
