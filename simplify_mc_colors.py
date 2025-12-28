import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# New MC Token section - minimal colors: white, black, dark gray only
new_mc_section = '''<!-- MC TOKEN SECTION -->
    <div id="mctoken" class="content-section">
    <section class="section">
        <div class="container">
            <div class="section-header">
                <div class="section-label">$MC TOKEN</div>
                <h2 class="section-title">MassaConnect Token</h2>
                <p class="section-desc">The official community token powering the MassaConnect ecosystem.</p>
            </div>

            <!-- Fair Launch Badge -->
            <div style="display: flex; justify-content: center; margin-bottom: 40px;">
                <div class="feature-card" style="display: inline-flex; align-items: center; gap: 12px; padding: 14px 28px; border-radius: 100px;">
                    <svg width="20" height="20" fill="white" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                    <span style="color: white; font-weight: 700; font-size: 0.9rem;">FAIR LAUNCH - No Pre-sale, No VC, 100% Community</span>
                </div>
            </div>

            <!-- Tokenomics Cards -->
            <div class="features-grid" style="grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); margin-bottom: 48px;">
                <div class="feature-card" style="text-align: center;">
                    <div class="tech-icon" style="margin: 0 auto 20px;">
                        <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v12M6 12h12"/></svg>
                    </div>
                    <div style="font-size: 2.5rem; font-weight: 800; color: white; margin-bottom: 8px;">23M</div>
                    <p>Total Supply</p>
                </div>
                <div class="feature-card" style="text-align: center;">
                    <div class="tech-icon" style="margin: 0 auto 20px;">
                        <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
                    </div>
                    <div style="font-size: 2.5rem; font-weight: 800; color: white; margin-bottom: 8px;">83.1%</div>
                    <p>In Liquidity Pool</p>
                    <span style="color: rgba(255,255,255,0.5); font-size: 0.75rem;">~19.1M MC</span>
                </div>
                <div class="feature-card" style="text-align: center;">
                    <div class="tech-icon" style="margin: 0 auto 20px;">
                        <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M20 12v10H4V12"/><rect x="2" y="7" width="20" height="5"/><line x1="12" y1="22" x2="12" y2="7"/><path d="M12 7H7.5a2.5 2.5 0 010-5C11 2 12 7 12 7z"/><path d="M12 7h4.5a2.5 2.5 0 000-5C13 2 12 7 12 7z"/></svg>
                    </div>
                    <div style="font-size: 2.5rem; font-weight: 800; color: white; margin-bottom: 8px;">1M</div>
                    <p>Community Airdrop</p>
                    <span style="color: rgba(255,255,255,0.5); font-size: 0.75rem;">For Early Adopters</span>
                </div>
                <div class="feature-card" style="text-align: center;">
                    <div class="tech-icon" style="margin: 0 auto 20px;">
                        <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
                    </div>
                    <div style="font-size: 2.5rem; font-weight: 800; color: white; margin-bottom: 8px;">2.9M</div>
                    <p>Development Fund</p>
                    <span style="color: rgba(255,255,255,0.5); font-size: 0.75rem;">Project Growth</span>
                </div>
            </div>

            <!-- Distribution Bar -->
            <div class="feature-card" style="margin-bottom: 48px;">
                <h3 style="font-size: 1.3rem; margin-bottom: 24px; text-align: center;">Token Distribution</h3>
                <div style="background: #1e293b; border-radius: 12px; height: 40px; overflow: hidden; display: flex; margin-bottom: 24px;">
                    <div style="width: 83.1%; background: #374151; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 0.8rem;">Pool 83.1%</div>
                    <div style="width: 4.3%; background: #4b5563;"></div>
                    <div style="width: 12.6%; background: #6b7280; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; font-size: 0.8rem;">Dev</div>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px;">
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <div style="width: 16px; height: 16px; background: #374151; border-radius: 4px;"></div>
                        <div>
                            <div style="color: white; font-weight: 600;">Liquidity Pool (DUSA)</div>
                            <div style="color: rgba(255,255,255,0.5); font-size: 0.8rem;">19,119,503 MC (83.1%)</div>
                        </div>
                    </div>
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <div style="width: 16px; height: 16px; background: #4b5563; border-radius: 4px;"></div>
                        <div>
                            <div style="color: white; font-weight: 600;">Community Airdrop</div>
                            <div style="color: rgba(255,255,255,0.5); font-size: 0.8rem;">1,000,000 MC (4.3%)</div>
                        </div>
                    </div>
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <div style="width: 16px; height: 16px; background: #6b7280; border-radius: 4px;"></div>
                        <div>
                            <div style="color: white; font-weight: 600;">Development Fund</div>
                            <div style="color: rgba(255,255,255,0.5); font-size: 0.8rem;">2,880,488 MC (12.6%)</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Airdrop Box -->
            <div class="feature-card" style="margin-bottom: 48px;">
                <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 20px;">
                    <div class="tech-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M20 12v10H4V12"/><rect x="2" y="7" width="20" height="5"/><line x1="12" y1="22" x2="12" y2="7"/><path d="M12 7H7.5a2.5 2.5 0 010-5C11 2 12 7 12 7z"/><path d="M12 7h4.5a2.5 2.5 0 000-5C13 2 12 7 12 7z"/></svg>
                    </div>
                    <div>
                        <h3 style="color: white; font-size: 1.2rem; margin: 0;">Community Airdrop Program</h3>
                        <p style="margin: 4px 0 0 0; font-size: 0.85rem;">1,000,000 MC for early supporters</p>
                    </div>
                </div>
                <div style="background: #1e293b; border-radius: 16px; padding: 24px;">
                    <h4 style="color: white; margin: 0 0 12px 0; font-size: 1rem;">How to Qualify:</h4>
                    <ul style="color: rgba(255,255,255,0.7); font-size: 0.9rem; margin: 0; padding-left: 20px; line-height: 2;">
                        <li>Download MassaConnect Wallet</li>
                        <li>Make your first swap MAS ↔ MC on DUSA DEX</li>
                        <li>Early adopters get bigger rewards!</li>
                    </ul>
                </div>
            </div>

            <!-- Contract Info -->
            <div class="feature-card" style="margin-bottom: 40px;">
                <div style="display: flex; align-items: center; justify-content: center; gap: 12px; margin-bottom: 28px;">
                    <div class="tech-icon">
                        <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>
                    </div>
                    <h3 style="font-size: 1.3rem; margin: 0; font-weight: 700;">Verified Contracts</h3>
                </div>

                <div style="display: grid; gap: 16px;">
                    <!-- Token Contract -->
                    <div style="background: #1e293b; border-radius: 16px; padding: 20px;">
                        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
                            <div class="new-icon">
                                <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
                            </div>
                            <div>
                                <div style="color: white; font-weight: 700; font-size: 0.95rem;">$MC Token Contract</div>
                                <div style="color: rgba(255,255,255,0.5); font-size: 0.75rem;">MRC-20 Standard</div>
                            </div>
                            <button onclick="navigator.clipboard.writeText('AS12XfRvGn4A8QZBmLSHsD2EBqpBVEsdF1CcbvJRTpqtXMYGhH6FH'); this.innerHTML='✓ Copied!'; setTimeout(()=>this.innerHTML='Copy', 2000)" style="margin-left: auto; padding: 8px 16px; background: #374151; border: none; border-radius: 8px; color: white; font-size: 0.8rem; cursor: pointer; font-weight: 600;">Copy</button>
                        </div>
                        <code style="display: block; background: #0f172a; padding: 12px 16px; border-radius: 10px; color: rgba(255,255,255,0.8); font-size: 0.78rem; word-break: break-all; font-family: monospace;">AS12XfRvGn4A8QZBmLSHsD2EBqpBVEsdF1CcbvJRTpqtXMYGhH6FH</code>
                    </div>

                    <!-- Pool Contract -->
                    <div style="background: #1e293b; border-radius: 16px; padding: 20px;">
                        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
                            <div class="new-icon">
                                <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
                            </div>
                            <div>
                                <div style="color: white; font-weight: 700; font-size: 0.95rem;">DUSA Liquidity Pool</div>
                                <div style="color: rgba(255,255,255,0.5); font-size: 0.75rem;">MC/WMAS Pair - V2</div>
                            </div>
                            <button onclick="navigator.clipboard.writeText('AS1tnZc9iWKrE77on7sVqZ5FqaHw81jVXjLChVT8vnmyxBKRRE93'); this.innerHTML='✓ Copied!'; setTimeout(()=>this.innerHTML='Copy', 2000)" style="margin-left: auto; padding: 8px 16px; background: #374151; border: none; border-radius: 8px; color: white; font-size: 0.8rem; cursor: pointer; font-weight: 600;">Copy</button>
                        </div>
                        <code style="display: block; background: #0f172a; padding: 12px 16px; border-radius: 10px; color: rgba(255,255,255,0.8); font-size: 0.78rem; word-break: break-all; font-family: monospace;">AS1tnZc9iWKrE77on7sVqZ5FqaHw81jVXjLChVT8vnmyxBKRRE93</code>
                    </div>

                    <!-- Badges -->
                    <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; padding-top: 8px;">
                        <span style="display: inline-flex; align-items: center; gap: 6px; padding: 8px 16px; background: #1e293b; border: 1px solid #374151; border-radius: 100px; color: white; font-size: 0.8rem; font-weight: 600;">
                            <svg width="14" height="14" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                            Verified on DUSA
                        </span>
                        <span style="display: inline-flex; align-items: center; gap: 6px; padding: 8px 16px; background: #1e293b; border: 1px solid #374151; border-radius: 100px; color: rgba(255,255,255,0.7); font-size: 0.8rem; font-weight: 500;">Bin Step: 20bps</span>
                        <span style="display: inline-flex; align-items: center; gap: 6px; padding: 8px 16px; background: #1e293b; border: 1px solid #374151; border-radius: 100px; color: rgba(255,255,255,0.7); font-size: 0.8rem; font-weight: 500;">Massa Blockchain</span>
                    </div>
                </div>
            </div>

            <!-- CTA Buttons -->
            <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">
                <a href="https://app.dusa.io/pools/AS12XfRvGn4A8QZBmLSHsD2EBqpBVEsdF1CcbvJRTpqtXMYGhH6FH/AS12U4TZfNK7qoLyEERBBRDMu8nm5MKoRzPXDXans4v9wdATZedz9/20/V2" target="_blank" class="btn btn-primary">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
                    Trade on DUSA
                </a>
                <a href="https://github.com/massaconnect/massaconnect/releases" class="btn btn-secondary" style="background: white; color: #0f172a;">
                    <svg width="18" height="18" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z" clip-rule="evenodd"/></svg>
                    Get Wallet
                </a>
            </div>
        </div>
    </section>
    </div><!-- END MC TOKEN SECTION -->'''

# Replace MC Token section
pattern = r'<!-- MC TOKEN SECTION -->.*?<!-- END MC TOKEN SECTION -->'
content = re.sub(pattern, new_mc_section, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ MC Token section updated - now using only white, black, and dark grays!")
