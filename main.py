#!/usr/bin/env python3
"""Persian Text Analyzer - Analyze Persian text statistics."""
import argparse
import re
import sys
from collections import Counter
def count_words(text):
    """Count the number of words in the text."""
    words = re.findall(r'\b\w+\b', text)
    return len(words)
def count_characters(text):
    """Count the number of characters including spaces."""
    return len(text)
def count_letters(text):
    """Count only alphabetic characters."""
    letters = re.findall(r'[^\W\d_]', text, re.UNICODE)
    return len(letters)
def count_sentences(text):
    """Count sentences based on punctuation."""
    sentences = re.split(r'[.!?؟؟\n]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)
def character_frequency(text):
    """Return frequency of each character."""
    counter = Counter(text)
    return dict(counter.most_common())
def word_frequency(text):
    """Return frequency of each word."""
    words = re.findall(r'\b\w+\b', text.lower())
    counter = Counter(words)
    return dict(counter.most_common())
def most_common_words(text, n=10):
    """Return top n most common words."""
    words = re.findall(r'\b\w+\b', text.lower())
    counter = Counter(words)
    return counter.most_common(n)
def analyze(text):
    """Analyze text and return a dictionary of statistics."""
    return {
        'word_count': count_words(text),
        'character_count': count_characters(text),
        'letter_count': count_letters(text),
        'sentence_count': count_sentences(text),
        'character_frequency': character_frequency(text),
        'word_frequency': word_frequency(text),
        'most_common_words': most_common_words(text, 10),
    }
def format_analysis(stats):
    """Format analysis statistics for display."""
    lines = []
    lines.append(f"تعداد کلمات: {stats['word_count']}")
    lines.append(f"تعداد کاراکترها (شامل فاصله): {stats['character_count']}")
    lines.append(f"تعداد حروف: {stats['letter_count']}")
    lines.append(f"تعداد جملات: {stats['sentence_count']}")
    lines.append("")
    lines.append("فراوانی کاراکترها:")
    for char, count in list(stats['character_frequency'].items())[:20]:
        lines.append(f"  {char}: {count}")
    lines.append("")
    lines.append("کلمات پرتکرار:")
    for word, count in stats['most_common_words']:
        lines.append(f"  {word}: {count}")
    return "\n".join(lines)
def main():
    parser = argparse.ArgumentParser(
        description="تحلیلگر متن فارسی - تحلیل متن فارسی و ارائه آمار",
        epilog="Example: python main.py --text 'متن فارسی خود را اینجا بنویسید'"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--text', '-t', help='متن ورودی برای تحلیل')
    group.add_argument('--file', '-f', help='مسیر فایل متنی برای تحلیل')
    group.add_argument('--stdin', '-s', action='store_true', help='خواندن متن از ورودی استاندارد')
    parser.add_argument('--top', '-n', type=int, default=10,
                        help='تعداد کلمات پرتکرار برای نمایش (پیش‌ فرض: 10)')
    parser.add_argument('--output', '-o', help='ذخیره خروجی در فایل')
    args = parser.parse_args()
    if args.text:
        text = args.text
    elif args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Error: فایل '{args.file}' یافت نشد", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error: خواندن فایل ناموفق: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.stdin:
        text = sys.stdin.read()
    else:
        print("Error: هیچ ورودی ارائه نشده", file=sys.stderr)
        sys.exit(1)
    if not text.strip():
        print("Error: متن ورودی خالی است", file=sys.stderr)
        sys.exit(1)
    stats = analyze(text)
    stats['most_common_words'] = most_common_words(text, args.top)
    output = format_analysis(stats)
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"نتیجه در فایل '{args.output}' ذخیره شد.")
        except Exception as e:
            print(f"Error: نوشتن فایل ناموفق: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(output)
if __name__ == '__main__':
    main()
