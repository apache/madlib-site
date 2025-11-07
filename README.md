# Apache MADlib Website

This is a restructured version of the Apache MADlib website using Material for MkDocs framework.

## Project Structure

```
├── mkdocs.yml                 # Main configuration file
├── docs/                      # Documentation source files
│   ├── index.md              # Homepage
│   ├── documentation/        # User guides and documentation
│   ├── api/                  # API documentation
│   ├── community/            # Community resources
│   ├── blog/                 # Blog posts and announcements
│   ├── team/                 # Team information
│   ├── asf/                  # ASF related information
│   ├── download.md           # Download page
│   └── assets/               # Static assets (CSS, JS, images)
├── community-artifacts/      # Jupyter notebooks and examples
└── README.md                 # This file
```

## Installation & Usage

1. **Install MkDocs and Material theme:**
   ```bash
   pip install mkdocs mkdocs-material
   ```

2. **Navigate to project directory:**
   ```bash
   cd madlib-site
   ```

3. **Serve locally for development:**
   ```bash
   mkdocs serve
   ```

4. **Build for production:**
   ```bash
   mkdocs build
   ```

## Customization

### Styling
- Custom CSS in `docs/assets/stylesheets/extra.css`
- Material theme configuration in `mkdocs.yml`

### Content
- All content is in Markdown format
- Easy to edit and maintain
- Supports Material for MkDocs extensions

## Assets Required

The website assets are located in the `docs/assets/` directory.

## Configuration

The `mkdocs.yml` file contains:
- Site metadata and branding
- Theme configuration with Material design
- Navigation structure
- Plugin configuration
- Markdown extensions

For more information, see the [MkDocs documentation](https://www.mkdocs.org/docs/) and [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/).