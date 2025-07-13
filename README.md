# MediAssist AI - Azure-Powered Medical Support System

A comprehensive medical AI assistant built on Azure OpenAI services, providing intelligent medical query processing, image analysis, and appointment booking capabilities.

## 🚀 Features

### Core Capabilities
- **Multi-Agent Medical AI System**: Specialized agents for clinical cases, literature research, symptom analysis, drug interactions, and nutrition guidance
- **Intelligent Query Routing**: Automatic detection and routing of medical queries to appropriate specialist agents
- **Medical Image Analysis**: Advanced image analysis using Azure OpenAI with intelligent fallback systems
- **Appointment Booking**: Integrated appointment scheduling with Azure Communication Services email notifications
- **Semantic Search**: Azure OpenAI-powered embeddings for accurate medical information retrieval

### Technical Highlights
- **Azure-First Architecture**: Built on Azure OpenAI, Azure Communication Services, and Azure best practices
- **Fallback Systems**: Robust error handling with intelligent fallback mechanisms
- **Caching & Performance**: Optimized caching for embeddings and responses
- **Security-Focused**: Environment-based configuration with no hardcoded credentials
- **Production-Ready**: Comprehensive logging, monitoring, and error handling

## 🏗️ Architecture

### Primary Services
- **Azure OpenAI Service**: Text generation, embeddings, and image analysis
- **Azure Communication Services**: Email notifications for appointments
- **Flask Web Framework**: RESTful API and web interface

### Agent System
- **Router Agent**: Intelligent query classification and routing
- **Clinical Agent**: Medical case analysis and treatment recommendations
- **Literature Agent**: Medical research and evidence-based information
- **Symptom Agent**: Symptom analysis and diagnostic suggestions
- **Drug Agent**: Medication information and interaction analysis
- **Diet Agent**: Nutritional guidance and diet planning
- **Image Agent**: Medical image analysis and interpretation

## 📋 Prerequisites

### System Requirements
- Python 3.8 or higher
- Azure OpenAI Service subscription
- Azure Communication Services subscription
- 4GB+ RAM recommended

### Azure Services Setup
1. **Azure OpenAI Service**:
   - Create an Azure OpenAI resource
   - Deploy GPT-4 or GPT-4o-mini model
   - Deploy text-embedding-3-small model
   - Note the endpoint and API key

2. **Azure Communication Services**:
   - Create Communication Services resource
   - Configure email domain
   - Note the connection string

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone <repository-url>
cd semantic_hackethon
python setup.py  # Automated setup script
```

### 2. Configure Environment
Copy the `.env` file and update with your Azure credentials:
```env
# Azure OpenAI Configuration
AZURE_OPENAI_API_KEY=your_azure_openai_api_key_here
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-01
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o-mini
AZURE_OPENAI_MODEL_NAME=gpt-4o-mini
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small
AZURE_OPENAI_EMBEDDING_MODEL=text-embedding-3-small

# Azure Communication Services
AZURE_COMMUNICATION_CONNECTION_STRING=your_connection_string_here
AZURE_COMMUNICATION_SENDER_EMAIL=donotreply@your-domain.com

# Application Configuration
SECRET_KEY=your_secret_key_here
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 📊 Data Requirements

Place the following Excel files in the `data/` directory:
- `clinical_cases.xlsx` - Medical case studies
- `drug_interactions.xlsx` - Drug interaction data
- `medical_literature.xlsx` - Research papers and studies
- `symptom_cases.xlsx` - Symptom-diagnosis mappings

## 🔧 Configuration

### Environment Variables
| Variable | Description | Required |
|----------|-------------|----------|
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API key | Yes |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI service endpoint | Yes |
| `AZURE_COMMUNICATION_CONNECTION_STRING` | Azure Communication Services connection string | Yes |
| `AZURE_COMMUNICATION_SENDER_EMAIL` | Sender email for notifications | Yes |
| `GOOGLE_AI_API_KEY` | Google AI API key for image analysis fallback | Optional |

### Application Settings
- `FLASK_ENV`: Set to 'production' for production deployment
- `FLASK_DEBUG`: Set to 'False' for production
- `SECRET_KEY`: Strong secret key for session management

## 🏥 Usage

### Medical Query Processing
1. Navigate to the main interface
2. Enter your medical question
3. The system automatically routes to the appropriate specialist agent
4. Receive comprehensive, formatted medical analysis

### Image Analysis
1. Go to the Image Analysis tab
2. Upload a medical image
3. Provide context about what you want analyzed
4. Get detailed medical image interpretation

### Appointment Booking
1. Use the appointment booking interface
2. Select doctor and time slot
3. Provide patient information
4. Receive email confirmation automatically

## 🔍 API Endpoints

### Core Endpoints
- `GET /` - Main web interface
- `POST /query` - Process medical queries
- `POST /analyze-image` - Medical image analysis
- `POST /book-appointment` - Book medical appointments
- `GET /status` - Application health status

### Utility Endpoints
- `POST /refresh-embeddings` - Refresh knowledge base embeddings
- `GET /health` - Detailed health check
- `POST /generate-specialists` - Generate specialist recommendations

## 🛡️ Security

### Best Practices Implemented
- **No Hardcoded Credentials**: All sensitive information via environment variables
- **Secure Communication**: HTTPS-ready configuration
- **Input Validation**: Comprehensive input sanitization
- **Error Handling**: Secure error responses without sensitive information
- **Rate Limiting**: Built-in protection against abuse

### Azure Security Features
- **Azure OpenAI**: Enterprise-grade security and compliance
- **Azure Communication Services**: Secure email delivery
- **Managed Identity Ready**: Easy integration with Azure Managed Identity

## 📈 Monitoring & Logging

### Application Logging
- Comprehensive logging to `app.log`
- Error tracking and performance monitoring
- Azure Application Insights ready

### Health Monitoring
- Real-time health checks
- Service dependency monitoring
- Performance metrics tracking

## 🔧 Troubleshooting

### Common Issues
1. **Azure OpenAI Connection Issues**:
   - Verify API key and endpoint
   - Check model deployment status
   - Ensure sufficient quota

2. **Email Not Sending**:
   - Verify Azure Communication Services configuration
   - Check domain verification status
   - Validate sender email address

3. **Image Analysis Failing**:
   - Ensure image format is supported (PNG, JPEG)
   - Check image size limits
   - Verify model supports vision capabilities

### Debug Mode
Enable debug mode for detailed error information:
```bash
export FLASK_DEBUG=True
python app.py
```

## 📚 Documentation

- `AZURE_MIGRATION.md` - Detailed migration guide and architecture overview
- `API_DOCUMENTATION.md` - Comprehensive API documentation
- `DEPLOYMENT_GUIDE.md` - Production deployment instructions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For issues and questions:
1. Check the troubleshooting section
2. Review the logs for error details
3. Consult the Azure service documentation
4. Create an issue in the repository

## 🚀 Future Enhancements

- **Azure Managed Identity**: Enhanced security with managed identity
- **Azure Cognitive Services**: Integration with additional AI services
- **Real-time Chat**: WebSocket-based real-time medical consultations
- **Mobile App**: React Native mobile application
- **Advanced Analytics**: Usage analytics and insights dashboard

---

Built with ❤️ using Azure OpenAI and modern web technologies.
