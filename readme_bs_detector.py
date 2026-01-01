#!/usr/bin/env python3
"""
README GPT Bullshit Detector - Because "revolutionary AI-powered synergy" doesn't compile.
"""

import re
import sys
from pathlib import Path

# The definitive list of phrases that scream "I asked ChatGPT to make me sound smart"
BUZZWORD_BINGO = [
    # The classics
    r'\brevolutionary\b', r'\bdisruptive\b', r'\bparadigm shift\b',
    # AI word salad
    r'\bAI.*powered\b', r'\bcutting.*edge\b', r'\bnext.*generation\b',
    # Corporate nonsense
    r'\bsynergy\b', r'\bleverage\b', r'\bholistic\b',
    # Vague promises
    r'\bseamless.*integration\b', r'\benterprise.*grade\b', r'\bscalable.*solution\b',
    # Empty adjectives
    r'\binnovative\b', r'\bgroundbreaking\b', r'\btransformative\b'
]

def detect_bullshit(text):
    """Returns buzzword count and sample sentences - higher score = more likely written by a robot trying to sound human."""
    hits = []
    total_score = 0
    
    for line in text.split('\n'):
        line_score = 0
        for pattern in BUZZWORD_BINGO:
            if re.search(pattern, line, re.IGNORECASE):
                line_score += 1
        if line_score > 0:
            hits.append(f"[{line_score}] {line.strip()[:80]}")
            total_score += line_score
    
    return total_score, hits[:5]  # Top 5 offenders only

def main():
    if len(sys.argv) != 2:
        print("Usage: python readme_bs_detector.py <README_FILE>")
        print("Example: python readme_bs_detector.py README.md")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Error: {file_path} not found. Much like the actual functionality in some READMEs.")
        sys.exit(1)
    
    try:
        content = file_path.read_text(encoding='utf-8')
        score, examples = detect_bullshit(content)
        
        print(f"\n📊 README Bullshit Analysis for: {file_path.name}")
        print(f"Total Buzzword Score: {score}")
        
        if score == 0:
            print("✅ Surprisingly coherent! Might have been written by an actual human.")
        elif score < 5:
            print("⚠️  Mild AI contamination. Probably just used for proofreading.")
        elif score < 15:
            print("🚨 Significant buzzword density. Author definitely asked ChatGPT to 'make it sound professional'.")
        else:
            print("💀 CRITICAL LEVELS DETECTED! This README contains more buzzwords than actual information.")
        
        if examples:
            print(f"\nTop {len(examples)} offending lines:")
            for example in examples:
                print(f"  {example}")
        
        # Bonus: Calculate BS percentage (because why not)
        word_count = len(content.split())
        if word_count > 0:
            bs_percent = (score / word_count) * 100
            print(f"\n📈 Buzzword Density: {bs_percent:.1f}% of words are marketing fluff")
            
    except Exception as e:
        print(f"Error reading file: {e}. But hey, at least the error message is honest!")

if __name__ == "__main__":
    main()
