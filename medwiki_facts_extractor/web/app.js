/**
 * MedWiki Facts Extractor - Web Visualization
 * Handles loading, filtering, and displaying extracted medical facts
 */

class MedWikiViewer {
    constructor() {
        this.articles = [];
        this.allTopics = new Set();
        this.allKeywords = new Set();
        this.filteredArticles = [];
        this.currentFilters = {
            search: '',
            topic: '',
            keyword: ''
        };
        this.init();
    }

    async init() {
        console.log('Initializing MedWiki Viewer...');
        await this.loadData();
        this.setupEventListeners();
        this.renderArticles();
    }

    async loadData() {
        try {
            // Try to load from the output directory first
            const response = await fetch('../output/extracted_data.json');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            this.articles = await response.json();
            console.log(`Loaded ${this.articles.length} articles`);

            // Extract unique topics and keywords
            this.articles.forEach(article => {
                if (article.topics) {
                    article.topics.forEach(topic => this.allTopics.add(topic));
                }
                if (article.keywords) {
                    article.keywords.forEach(keyword => this.allKeywords.add(keyword));
                }
            });

            this.populateFilters();
        } catch (error) {
            console.error('Error loading data:', error);
            this.showNoResults();
        }
    }

    populateFilters() {
        // Sort and populate topic filter
        const topics = Array.from(this.allTopics).sort();
        const topicSelect = document.getElementById('topicFilter');
        topics.forEach(topic => {
            const option = document.createElement('option');
            option.value = topic;
            option.textContent = topic;
            topicSelect.appendChild(option);
        });

        // Sort and populate keyword filter
        const keywords = Array.from(this.allKeywords).sort();
        const keywordSelect = document.getElementById('keywordFilter');
        keywords.forEach(keyword => {
            const option = document.createElement('option');
            option.value = keyword;
            option.textContent = keyword;
            keywordSelect.appendChild(option);
        });
    }

    setupEventListeners() {
        document.getElementById('searchInput').addEventListener('input', (e) => {
            this.currentFilters.search = e.target.value.toLowerCase();
            this.applyFilters();
        });

        document.getElementById('topicFilter').addEventListener('change', (e) => {
            this.currentFilters.topic = e.target.value;
            this.applyFilters();
        });

        document.getElementById('keywordFilter').addEventListener('change', (e) => {
            this.currentFilters.keyword = e.target.value;
            this.applyFilters();
        });

        document.getElementById('resetFilters').addEventListener('click', () => {
            this.resetFilters();
        });
    }

    applyFilters() {
        this.filteredArticles = this.articles.filter(article => {
            // Search filter
            const matchesSearch = !this.currentFilters.search ||
                article.title.toLowerCase().includes(this.currentFilters.search) ||
                article.summary.toLowerCase().includes(this.currentFilters.search);

            // Topic filter
            const matchesTopic = !this.currentFilters.topic ||
                (article.topics && article.topics.includes(this.currentFilters.topic));

            // Keyword filter
            const matchesKeyword = !this.currentFilters.keyword ||
                (article.keywords && article.keywords.includes(this.currentFilters.keyword));

            return matchesSearch && matchesTopic && matchesKeyword;
        });

        this.renderArticles();
        this.updateStats();
    }

    resetFilters() {
        document.getElementById('searchInput').value = '';
        document.getElementById('topicFilter').value = '';
        document.getElementById('keywordFilter').value = '';
        this.currentFilters = {
            search: '',
            topic: '',
            keyword: ''
        };
        this.applyFilters();
    }

    renderArticles() {
        const container = document.getElementById('articlesContainer');
        const noResults = document.getElementById('noResults');

        if (this.filteredArticles.length === 0) {
            container.innerHTML = '';
            noResults.style.display = 'block';
            return;
        }

        noResults.style.display = 'none';
        container.innerHTML = this.filteredArticles
            .map(article => this.createArticleCard(article))
            .join('');
    }

    createArticleCard(article) {
        const factsHtml = article.key_facts
            .map(fact => `
                <div class="fact-item">
                    <div class="fact-text">• ${this.escapeHtml(fact.fact)}</div>
                    <div class="supporting-text">
                        <strong>Supporting:</strong> ${this.escapeHtml(fact.supporting_statement)}
                    </div>
                </div>
            `).join('');

        const topicTags = (article.topics || [])
            .map(topic => `<span class="tag" onclick="viewer.filterByTopic('${topic}')">${this.escapeHtml(topic)}</span>`)
            .join('');

        const keywordTags = (article.keywords || [])
            .map(keyword => `<span class="tag" onclick="viewer.filterByKeyword('${keyword}')">${this.escapeHtml(keyword)}</span>`)
            .join('');

        return `
            <div class="article-card">
                <div class="article-id">Article #${this.escapeHtml(article.medwiki_id)}</div>
                <h2 class="article-title">${this.escapeHtml(article.title)}</h2>

                <div class="article-summary">
                    <strong>Summary:</strong><br>
                    ${this.escapeHtml(article.summary)}
                </div>

                <div class="key-facts">
                    <div class="key-facts-title">🔍 Key Facts</div>
                    ${factsHtml}
                </div>

                <div class="metadata">
                    <div class="metadata-group">
                        <div class="metadata-title">Topics</div>
                        <div class="tags">${topicTags || '<span class="tag">None</span>'}</div>
                    </div>
                    <div class="metadata-group">
                        <div class="metadata-title">Keywords</div>
                        <div class="tags">${keywordTags || '<span class="tag">None</span>'}</div>
                    </div>
                </div>
            </div>
        `;
    }

    escapeHtml(text) {
        const map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        };
        return text.replace(/[&<>"']/g, m => map[m]);
    }

    filterByTopic(topic) {
        document.getElementById('topicFilter').value = topic;
        this.currentFilters.topic = topic;
        this.applyFilters();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    filterByKeyword(keyword) {
        document.getElementById('keywordFilter').value = keyword;
        this.currentFilters.keyword = keyword;
        this.applyFilters();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    showNoResults() {
        document.getElementById('articlesContainer').innerHTML = '';
        document.getElementById('noResults').style.display = 'block';
    }

    updateStats() {
        document.getElementById('articleCount').textContent = this.articles.length;
        document.getElementById('visibleCount').textContent = this.filteredArticles.length;
    }
}

// Initialize the viewer when DOM is ready
let viewer;
document.addEventListener('DOMContentLoaded', () => {
    viewer = new MedWikiViewer();
});
