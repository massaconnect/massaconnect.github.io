import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update the section description
content = content.replace(
    'Enhanced visual design and improved user experience across the entire app',
    'App rebrand, $MC token integration, S1 key import, and visual improvements'
)

# Update date to December 2024 -> December 2024 (already correct but let's ensure)
content = content.replace('December 2024', 'December 2024')

# Update changelog for v1.3.0 with new features
old_changelog = '''<!-- v1.3.0 -->
                <div class="changelog-version">
                    <div class="changelog-header">
                        <h3>v1.3.0</h3>
                        <span class="changelog-date">December 2024</span>
                        <span class="changelog-tag tag-latest">Latest</span>
                    </div>
                    <div class="changelog-content">
                        <div class="changelog-category">
                            <h4>✨ UI Improvements</h4>
                            <ul>
                                <li>Unified visual styles across Staking, Portfolio, Charts and About sections</li>
                                <li>Consistent icon styling (black/white containers matching theme)</li>
                                <li>Improved About dialog with proper icon design</li>
                                <li>Fixes to bidirectional NFT search synchronization for faster finding</li>
                            </ul>
                        </div>
                        <div class="changelog-category">
                            <h4>✨ Technical</h4>
                            <ul>
                                <li>versionCode: 7</li>
                                <li>versionName: 1.3.0</li>
                            </ul>
                        </div>
                    </div>
                </div>'''

new_changelog = '''<!-- v1.3.0 -->
                <div class="changelog-version">
                    <div class="changelog-header">
                        <h3>v1.3.0</h3>
                        <span class="changelog-date">December 2024</span>
                        <span class="changelog-tag tag-latest">Latest</span>
                    </div>
                    <div class="changelog-content">
                        <div class="changelog-category">
                            <h4>✨ New Features</h4>
                            <ul>
                                <li><strong>App Rebrand:</strong> MassaPay → MassaConnect</li>
                                <li><strong>$MC Token:</strong> Native token integrated in swap</li>
                                <li><strong>S1 Key Import:</strong> Import S1 private keys from within the app</li>
                                <li><strong>DUSA Integration:</strong> $MC proposed as default swap pair</li>
                            </ul>
                        </div>
                        <div class="changelog-category">
                            <h4>✨ UI Improvements</h4>
                            <ul>
                                <li>Unified visual styles across all screens</li>
                                <li>Consistent icon styling (black/white containers)</li>
                                <li>Improved About dialog with new branding</li>
                                <li>Enhanced NFT search synchronization</li>
                            </ul>
                        </div>
                        <div class="changelog-category">
                            <h4>⚙️ Technical</h4>
                            <ul>
                                <li>versionCode: 7</li>
                                <li>versionName: 1.3.0</li>
                            </ul>
                        </div>
                    </div>
                </div>'''

# Try to replace with broken characters too
content = content.replace(old_changelog.replace('✨', 'âœ¨').replace('⚙️', 'âš™ï¸'), new_changelog)
content = content.replace(old_changelog, new_changelog)

# Update What's New cards to reflect new features
old_whats_new = '''<div class="new-grid">
                <div class="new-card">
                    <div class="new-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2.7 10.3a2.41 2.41 0 000 3.41l7.59 7.59a2.41 2.41 0 003.41 0l7.59-7.59a2.41 2.41 0 000-3.41l-7.59-7.59a2.41 2.41 0 00-3.41 0z"/></svg></div>
                    <div>
                        <span class="new-tag">New</span>
                        <h3>NFT Gallery Redesign</h3>
                        <p>Complete visual overhaul with hero cards and quick stats</p>
                    </div>
                </div>
                <div class="new-card">
                    <div class="new-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="13.5" cy="6.5" r="0.5"/><circle cx="17.5" cy="10.5" r="0.5"/><circle cx="8.5" cy="7.5" r="0.5"/><circle cx="6.5" cy="12.5" r="0.5"/><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c.926 0 1.648-.746 1.648-1.688 0-.437-.18-.835-.437-1.125-.29-.289-.438-.652-.438-1.125a1.64 1.64 0 011.668-1.668h1.996c3.051 0 5.555-2.503 5.555-5.555C21.965 6.012 17.461 2 12 2z"/></svg></div>
                    <div>
                        <span class="new-tag">Improved</span>
                        <h3>Accounts Dashboard</h3>'''

new_whats_new = '''<div class="new-grid">
                <div class="new-card">
                    <div class="new-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg></div>
                    <div>
                        <span class="new-tag">New</span>
                        <h3>$MC Token Integration</h3>
                        <p>Native MassaConnect token integrated in swap with DUSA</p>
                    </div>
                </div>
                <div class="new-card">
                    <div class="new-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg></div>
                    <div>
                        <span class="new-tag">New</span>
                        <h3>S1 Key Import</h3>'''

content = content.replace(old_whats_new, new_whats_new)

# Also update second card description
content = content.replace(
    '<h3>Accounts Dashboard</h3>\n                        <p>Sleek new design with gradient cards and activity feed</p>',
    '<h3>S1 Key Import</h3>\n                        <p>Import S1 private keys directly from within the app</p>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Updated version to 1.3.0 with new features in changelog and What's New!")
