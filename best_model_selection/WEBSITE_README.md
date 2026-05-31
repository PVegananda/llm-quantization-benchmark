# Interactive Website - LLM Quantization Benchmark

**Modern HTML/CSS/JS Interactive Documentation**

This folder contains a fully functional interactive website for exploring the LLM quantization benchmark analysis.

---

## Quick Start (2 minutes)

### Method 1: Open in Browser (Easiest)
```bash
# Simply open the HTML file in your browser
open index.html
# Or double-click index.html in Finder
```

### Method 2: Local Web Server (Recommended)
```bash
# If you have Python 3
python -m http.server 8000

# Or with Python 2
python -m SimpleHTTPServer 8000

# Or with Node.js
npx http-server
```
Then navigate to: `http://localhost:8000`

---

## What's Included

### Files
- **index.html** - Main website structure
- **styles.css** - Professional styling (1000+ lines)
- **script.js** - Interactive features and functionality
- **README.md** - This file

### Features

#### 📊 Overview Tab
- Key metrics at a glance
- Efficiency gains summary
- Data integrity verification
- Evaluation metrics explanation

#### 🏆 Model Rankings Tab
- Interactive results table
- Search functionality
- GPU filter buttons
- Multiple sort options (score, throughput, quality)
- Top 3 models showcase with medals
- Performance charts

#### 💡 Use Cases Tab
- 6 interactive scenario cards
- Clickable selection with detailed recommendations
- Model-specific reasoning
- Expected performance metrics

#### 🚀 Deployment Tab
- 5 sub-sections with code examples
- Copy-to-clipboard buttons for code blocks
- Setup instructions
- Model loading examples
- Inference patterns
- FastAPI server example
- Optimization tips

#### 📐 Methodology Tab
- 6-factor scoring visualization
- Weight explanation with badges
- Formula display
- Normalization method
- Weight justification
- Alternative weight presets
- Data validation checklist

#### ❓ FAQ Tab
- 9 comprehensive questions
- Click-to-expand answers
- Search functionality
- Index navigation

---

## Interactive Features

### Table Interactions
```
✓ Search by model name or GPU
✓ Filter by GPU (RTX4080, RTX4070, All)
✓ Sort by Score, Throughput, or Quality
✓ Click column headers to re-sort
✓ Highlight on hover
```

### Use Case Selection
```
✓ Click any scenario card
✓ Get instant recommendations
✓ See detailed reasoning
✓ Review performance expectations
✓ Close with X button
```

### Code Blocks
```
✓ Click "Copy" to copy code to clipboard
✓ Button shows "Copied!" confirmation
✓ All code formatted with syntax
✓ Supports Python, bash, and more
```

### Navigation
```
✓ Tab links in navbar
✓ Smooth transitions between sections
✓ Responsive mobile menu
✓ Direct access to any section
```

### FAQ Search
```
✓ Type to filter questions
✓ Only matching FAQs shown
✓ Click to expand answer
```

---

## Customization

### Colors
Edit `:root` variables in `styles.css`:
```css
:root {
    --primary: #2563eb;        /* Main color */
    --secondary: #10b981;      /* Accent color */
    --dark: #1f2937;          /* Text color */
    /* ... more colors ... */
}
```

### Data Updates
Edit model data in `script.js`:
```javascript
const modelsData = [
    {
        model: "GPT-2",
        gpu: "RTX4080",
        score: 0.7234,
        throughput: 127.36,
        // ... etc
    }
];
```

### Add New Use Case
In `script.js`, add to `useCases` object:
```javascript
const useCases = {
    mycase: {
        title: "My Custom Use Case",
        recommendation: "Model Name",
        // ... details
    }
};
```

---

## Browser Compatibility

✅ **Modern Browsers:**
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

✅ **Features:**
- CSS Grid & Flexbox
- CSS Custom Properties (Variables)
- ES6 JavaScript
- Clipboard API

---

## Mobile Responsive

- ✅ Mobile-first design
- ✅ Responsive breakpoints at 768px and 480px
- ✅ Touch-friendly buttons and inputs
- ✅ Readable on all screen sizes

---

## File Sizes

| File | Size | Purpose |
|------|------|---------|
| index.html | ~35 KB | Structure |
| styles.css | ~30 KB | Styling |
| script.js | ~15 KB | Functionality |
| **Total** | **~80 KB** | Lightweight |

No external dependencies - everything self-contained!

---

## Features Breakdown

### Search & Filter
- Real-time search across model names
- GPU-based filtering
- Dynamic table updates
- No page reload needed

### Sorting
- Sort by composite score
- Sort by throughput
- Sort by quality metrics
- Clickable column headers

### Copy-to-Clipboard
- One-click code copying
- Visual feedback
- Works on all browsers
- Automatic timeout

### Responsive Design
- Mobile-optimized
- Tablet-friendly
- Desktop-optimized
- Flexible grid layouts

### Accessibility
- Semantic HTML
- Color contrast compliance
- Keyboard navigation
- Clear focus states

---

## Performance

- **Load Time:** <1 second
- **Interactivity:** Instant (no server calls)
- **Size:** ~80 KB total
- **Resources:** Zero dependencies

---

## Offline Use

This website is completely offline - no internet required!
- ✅ All content bundled
- ✅ No API calls
- ✅ No external resources
- ✅ Works locally

---

## Use Cases

### 👨‍💼 Business Decision Makers
1. Open Overview tab for quick summary
2. Check Model Rankings for top performers
3. Use Use Cases selector for your scenario
4. View expected costs in deployment guide

### 👨‍💻 Developers
1. Go to Deployment tab
2. Copy code examples
3. Follow setup instructions
4. Customize for your needs

### 📚 Researchers
1. Read Methodology tab in detail
2. Understand weight justification
3. Explore FAQ for questions
4. Customize weights for your priorities

### 👨‍🎓 Students
1. Start with Overview
2. Explore Model Rankings
3. Learn from Use Cases
4. Study Methodology
5. Reference FAQ

---

## Extending the Website

### Add New Model
1. Add to `modelsData` in `script.js`
2. Table updates automatically
3. Rankings recalculate

### Add New Use Case
1. Add to `useCases` in `script.js`
2. Create new `.use-case-card` in HTML
3. Fully integrated

### Custom Styling
1. Edit `styles.css`
2. Change colors, fonts, spacing
3. No rebuild needed

### New Sections
1. Add `<section id="new">` in HTML
2. Add tab link in navbar
3. Add content and styling
4. Add JavaScript handler

---

## Troubleshooting

### Styles Not Loading?
- Check file names (case-sensitive on Mac/Linux)
- Verify all three files in same folder
- Clear browser cache
- Try different browser

### JavaScript Not Working?
- Check browser console for errors
- Enable JavaScript (usually enabled by default)
- Try without ad blockers
- Check file permissions

### Can't Copy Code?
- Some browsers require HTTPS for Clipboard API
- Alternative: Select text manually (Cmd+C / Ctrl+C)
- Works on localhost without HTTPS

### Mobile Issues?
- Ensure browser is up-to-date
- Try landscape orientation
- Clear app cache
- Try different browser

---

## Browser Console

Open browser console (F12) to debug:
- Check for JavaScript errors
- Monitor performance
- See console logs
- Debug interactive features

---

## Next Steps

1. **Open:** Double-click `index.html` or use `open index.html`
2. **Explore:** Click through tabs to explore content
3. **Interact:** Try searching, filtering, copying code
4. **Customize:** Edit colors or data as needed
5. **Share:** Deploy to any web server

---

## Features Summary

| Feature | Status | Notes |
|---------|--------|-------|
| Overview | ✅ | 4 metric cards + detailed info |
| Model Rankings | ✅ | Searchable, filterable, sortable table |
| Use Cases | ✅ | 6 interactive scenarios |
| Deployment | ✅ | Code examples with copy buttons |
| Methodology | ✅ | Visual weight explanation |
| FAQ | ✅ | Searchable Q&A |
| Mobile | ✅ | Fully responsive |
| Offline | ✅ | No internet required |
| Dark Mode | ⏳ | Can be added |
| Print | ✅ | CSS supports printing |

---

## Production Deployment

### Deploy to GitHub Pages
```bash
# Push all files to gh-pages branch
# Website accessible at username.github.io/project
```

### Deploy to Netlify
```bash
# Drag-and-drop folder to Netlify
# Get live URL in seconds
# No configuration needed
```

### Deploy to Own Server
```bash
# Copy all files to web server
# Serve via HTTP/HTTPS
# Works with any web server (Apache, Nginx, etc)
```

---

## Resources

### Modern Web Standards Used
- HTML5
- CSS3 (Flexbox, Grid, Custom Properties)
- ES6+ JavaScript
- Responsive Web Design

### Browser Standards
- Semantic HTML
- Accessible Color Contrast
- Touch-friendly Interface
- Keyboard Navigation Support

---

## License & Attribution

Based on: **Oprea, S.-V., & Bâra, A. (2026)**
"Quantized Transformers in Practice: Benchmarking Full- and Low-Precision LLMs Across Two Processors"

---

## Support

**For Technical Help:**
- Check browser console (F12)
- Verify file names and paths
- Ensure all 3 files in same folder
- Try different browser

**For Content Questions:**
- Review Methodology tab
- Check FAQ section
- Read Use Cases guide
- Explore deployment guide

---

**Status:** ✅ Production Ready  
**Version:** 1.0  
**Last Updated:** May 31, 2026

**Ready to use! Open `index.html` now →**
