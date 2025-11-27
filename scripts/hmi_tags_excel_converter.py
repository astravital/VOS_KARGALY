"""
Скрипт для работы с HMI тегами WinCC Advanced V20.
Читает CSV файлы, позволяет редактировать данные и записывает обратно в Excel.

Использование:
    python hmi_tags_excel_converter.py --read-csv
    python hmi_tags_excel_converter.py --write-excel
    python hmi_tags_excel_converter.py --read-csv --write-excel
"""

import pandas as pd
import argparse
import os
from pathlib import Path

# Пути к файлам
PROJECT_ROOT = Path(__file__).parent.parent
HMI_TAGS_DIR = PROJECT_ROOT / "CURSOR_PROJECT" / "examples" / "HMI_TAGS"
CSV_HMI_TAGS = HMI_TAGS_DIR / "Hmi Tags.csv"
CSV_MULTIPLEXING = HMI_TAGS_DIR / "Multiplexing.csv"
EXCEL_FILE = HMI_TAGS_DIR / "HMITags.xlsx"


def read_csv_files():
    """
    Читает CSV файлы с HMI тегами и мультиплексированием.
    Использует точку с запятой как разделитель (стандарт для WinCC).
    """
    print(f"Чтение CSV файлов из {HMI_TAGS_DIR}")
    
    # Читаем HMI Tags CSV (разделитель - точка с запятой)
    try:
        df_hmi_tags = pd.read_csv(CSV_HMI_TAGS, sep=';', encoding='utf-8')
        print(f"✓ Прочитано {len(df_hmi_tags)} строк из 'Hmi Tags.csv'")
        print(f"  Колонки: {list(df_hmi_tags.columns)[:5]}... (всего {len(df_hmi_tags.columns)})")
    except Exception as e:
        print(f"✗ Ошибка при чтении 'Hmi Tags.csv': {e}")
        return None, None
    
    # Читаем Multiplexing CSV
    try:
        df_multiplexing = pd.read_csv(CSV_MULTIPLEXING, sep=';', encoding='utf-8')
        print(f"✓ Прочитано {len(df_multiplexing)} строк из 'Multiplexing.csv'")
        print(f"  Колонки: {list(df_multiplexing.columns)}")
    except Exception as e:
        print(f"✗ Ошибка при чтении 'Multiplexing.csv': {e}")
        return df_hmi_tags, None
    
    return df_hmi_tags, df_multiplexing


def write_to_excel(df_hmi_tags, df_multiplexing, output_file=None):
    """
    Записывает данные обратно в Excel файл с двумя вкладками.
    
    Args:
        df_hmi_tags: DataFrame с HMI тегами
        df_multiplexing: DataFrame с мультиплексированием
        output_file: Путь к выходному Excel файлу (по умолчанию HMITags.xlsx)
    """
    if output_file is None:
        output_file = EXCEL_FILE
    
    print(f"\nЗапись данных в Excel файл: {output_file}")
    
    try:
        # Создаем Excel writer с движком openpyxl
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            # Записываем HMI Tags на вкладку 'hmi_tags'
            if df_hmi_tags is not None:
                df_hmi_tags.to_excel(writer, sheet_name='hmi_tags', index=False)
                print(f"✓ Записано {len(df_hmi_tags)} строк на вкладку 'hmi_tags'")
            
            # Записываем Multiplexing на вкладку 'multiplexing'
            if df_multiplexing is not None:
                df_multiplexing.to_excel(writer, sheet_name='multiplexing', index=False)
                print(f"✓ Записано {len(df_multiplexing)} строк на вкладку 'multiplexing'")
        
        print(f"✓ Excel файл успешно создан: {output_file}")
        return True
    except Exception as e:
        print(f"✗ Ошибка при записи в Excel: {e}")
        print("  Убедитесь, что установлены библиотеки: pip install pandas openpyxl")
        return False


def show_dataframe_info(df, name):
    """Выводит информацию о DataFrame."""
    if df is None:
        print(f"\n{name}: Данные не загружены")
        return
    
    print(f"\n{name}:")
    print(f"  Строк: {len(df)}")
    print(f"  Колонок: {len(df.columns)}")
    print(f"  Первые колонки: {list(df.columns)[:10]}")
    print(f"\n  Первые 3 строки:")
    print(df.head(3).to_string())


def main():
    parser = argparse.ArgumentParser(
        description='Конвертер HMI тегов между CSV и Excel форматами для WinCC Advanced V20'
    )
    parser.add_argument('--read-csv', action='store_true',
                       help='Читать CSV файлы и показывать информацию')
    parser.add_argument('--write-excel', action='store_true',
                       help='Записать данные из CSV в Excel файл')
    parser.add_argument('--output', type=str, default=None,
                       help='Путь к выходному Excel файлу (по умолчанию HMITags.xlsx)')
    
    args = parser.parse_args()
    
    # Если не указаны аргументы, выполняем оба действия
    if not args.read_csv and not args.write_excel:
        args.read_csv = True
        args.write_excel = True
    
    # Читаем CSV файлы
    if args.read_csv or args.write_excel:
        df_hmi_tags, df_multiplexing = read_csv_files()
        
        if args.read_csv:
            show_dataframe_info(df_hmi_tags, "HMI Tags")
            show_dataframe_info(df_multiplexing, "Multiplexing")
        
        # Записываем в Excel
        if args.write_excel:
            if df_hmi_tags is not None or df_multiplexing is not None:
                write_to_excel(df_hmi_tags, df_multiplexing, args.output)
            else:
                print("\n✗ Нет данных для записи в Excel")


if __name__ == "__main__":
    main()

