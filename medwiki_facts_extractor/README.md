# MedWiki Facts Extractor

Extract structured facts from medical articles using MiniMax-M2 API and DSPy framework, with interactive HTML visualization.

## Features

✨ **Intelligent Extraction**
- 3-4 line summary of each article
- 5-6 key facts with supporting statements
- Automatic topic and keyword extraction

🎨 **Interactive Visualization**
- Beautiful HTML-based dashboard
- Filter by topics or keywords
- Full-text search across articles
- Responsive design for mobile and desktop

⚙️ **Modern Tech Stack**
- DSPy for structured LM outputs
- MiniMax-M2 API with OpenAI-compatible interface
- Python with `uv` for dependency management
- Static HTML/JS (no backend needed)

## Setup

### Prerequisites
- Python 3.10+
- `uv` package manager (install via `pip install uv`)
- MiniMax API key (provided in `idea.md`)

### Installation

```bash
# Install dependencies using uv
uv pip install -e .

# Or install specific packages
uv pip install dspy-ai litellm pydantic requests pandas
```

## Usage

### 1. Test Sample Extraction

Test the extraction pipeline with a sample article:

```bash
python test_sample.py
```

This will:
- Load a sample medical article
- Extract summary, facts, topics, and keywords
- Save results to `sample_output.json`

### 2. Process All Articles

Extract facts from all articles in the CSV:

```bash
python process_articles.py
```

This will:
- Read articles from `clirnet_articles.csv`
- Call MiniMax-M2 API for each article
- Save extracted data to `output/extracted_data.json`
- Show progress for each article

**Note:** Set `MINIMAX_API_KEY` environment variable to override the default key:
```bash
export MINIMAX_API_KEY="your_api_key_here"
```

### 3. View Results

Open the web visualization:

```bash
# Option 1: Simple HTTP server (Python 3.7+)
cd web
python -m http.server 8000

# Option 2: Using any other HTTP server
# Then open http://localhost:8000
```

Or simply open `web/index.html` in a browser (limited functionality without a server).

## Project Structure

```
medwiki_facts_extractor/
├── pyproject.toml              # Project configuration
├── extractor.py                # DSPy signatures & extraction logic
├── process_articles.py         # Main processing script
├── test_sample.py              # Test with sample article
├── clirnet_articles.csv        # Input articles
├── output/
│   └── extracted_data.json     # Generated: extracted facts (JSON)
└── web/
    ├── index.html              # Main visualization page
    ├── style.css               # Styling
    └── app.js                  # Frontend filtering & display logic
```

## Data Format

### Input CSV
Required columns:
- `medwiki_id`: Article ID
- `raw_title`: Article title
- `raw_description`: Article content/description

### Output JSON
```json
[
  {
    "medwiki_id": "1",
    "title": "Article Title",
    "summary": "3-4 line summary...",
    "key_facts": [
      {
        "fact": "Key fact statement",
        "supporting_statement": "Supporting evidence or explanation"
      }
    ],
    "topics": ["Topic1", "Topic2"],
    "keywords": ["keyword1", "keyword2"]
  }
]
```

## API Configuration

**Model:** MiniMax-M2
**Base URL:** https://api.minimax.io/v1
**API Key:** Stored in `idea.md` and `process_articles.py`

The API is called via DSPy's LM interface using OpenAI-compatible endpoints.

## Filtering & Search

The web interface supports:

1. **Text Search** - Search article titles and summaries
2. **Topic Filter** - Filter articles by medical topics
3. **Keyword Filter** - Filter articles by keywords
4. **Combined Filters** - Use multiple filters together

Click on any topic or keyword tag to instantly filter by that value.

## Customization

### Modify Extraction Fields

Edit `extractor.py` to change what gets extracted:
- Adjust prompt descriptions in `ExtractArticleSignature`
- Modify the number of facts, topics, or keywords

### Customize Styling

Edit `web/style.css` to change colors, layout, or responsive breakpoints.

### Advanced: Tool Use

The MiniMax-M2 model supports tool/function calling. You can extend the extraction to use tools for structured data lookup or validation.

## Troubleshooting

### API Key Issues
```bash
# Check if API key is valid
# The key format should start with "eyJhbGciOiJSUzI1NiI..."
```

### Import Errors
```bash
# Ensure all dependencies are installed
uv pip install dspy-ai litellm pydantic requests pandas
```

### JSON Parsing Errors
- Some API responses may have formatting issues
- The extractor has fallback error handling
- Check `sample_output.json` to verify format

### Browser Cache Issues
- Hard refresh (Ctrl+Shift+R or Cmd+Shift+R) when viewing web interface
- Clear browser cache if filters don't work

## Performance Notes

- Processing 20+ articles may take several minutes due to API latency
- Each article makes one API call (no batch processing)
- Results are cached in JSON for instant viewing

## Future Enhancements

- [ ] Batch API calls for faster processing
- [ ] Database storage (SQLite/PostgreSQL)
- [ ] Export to PDF/Excel
- [ ] Multi-language support
- [ ] Admin panel for managing extractions
- [ ] API endpoint for programmatic access

## License

Internal CLIRNET project

## Support

Contact: Arnab Saha (arnab.saha@clirnet.com)
