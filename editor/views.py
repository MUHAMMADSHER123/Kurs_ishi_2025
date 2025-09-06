from django.shortcuts import render
import io
import contextlib
import sys
import traceback
import os
import importlib
import builtins

# Barcha standart modullarga ruxsat berish
ALLOWED_MODULES = [
    'os', 'sys', 'math', 'random', 'datetime', 'time', 'json',
    're', 'collections', 'itertools', 'functools', 'operator',
    'string', 'array', 'struct', 'copy', 'pprint', 'typing'
]

# Xavfsiz built-in funksiyalar
SAFE_BUILTINS = {
    # Built-in funksiyalar
    'open': open,
    'dir': dir,
    'type': type,
    'isinstance': isinstance,
    'issubclass': issubclass,
    'len': len,
    'str': str,
    'int': int,
    'float': float,
    'list': list,
    'dict': dict,
    'tuple': tuple,
    'set': set,
    'bool': bool,
    'range': range,
    'sum': sum,
    'max': max,
    'min': min,
    'abs': abs,
    'round': round,
    'zip': zip,
    'enumerate': enumerate,
    'reversed': reversed,
    'sorted': sorted,
    'filter': filter,
    'map': map,
    'any': any,
    'all': all,
    'chr': chr,
    'ord': ord,
    'hex': hex,
    'bin': bin,
    'oct': oct,
    'hash': hash,
    'id': id,
    'callable': callable,
    'hasattr': hasattr,
    'getattr': getattr,
    'setattr': setattr,
    'delattr': delattr,
    'property': property,
    'staticmethod': staticmethod,
    'classmethod': classmethod,
    'super': super,
    'vars': vars,
    'locals': locals,
    'globals': globals,
    'compile': compile,
    'eval': eval,
    'exec': exec,
    'repr': repr,
    'ascii': ascii,
    'format': format,
    'divmod': divmod,
    'pow': pow,
    'round': round,
    'breakpoint': breakpoint,
    'memoryview': memoryview,
    'bytearray': bytearray,
    'bytes': bytes,
    'complex': complex,
    'frozenset': frozenset,
    'object': object,
    'slice': slice,
    'staticmethod': staticmethod,
    'type': type,
    'zip': zip,
    '__import__': __import__,
    'help': help,
    'input': input,
    'print': print,
}
    'print': print,
    'len': len,
    'str': str,
    'int': int,
    'float': float,
    'list': list,
    'dict': dict,
    'tuple': tuple,
    'set': set,
    'bool': bool,
    'range': range,
    'sum': sum,
    'max': max,
    'min': min,
    'abs': abs,
    'round': round,
    'zip': zip,
    'enumerate': enumerate,
    'reversed': reversed,
    'sorted': sorted,
    'isinstance': isinstance,
    'issubclass': issubclass,
    'type': type,
}

def check_restricted_code(code):
    """Xavfli kodlarni tekshirish (hozircha hech narsani cheklamaymiz)"""
    return True, ""

def execute_code(code):
    """Kodni ishga tushirish"""
    # Chiqish va xatolarni yig'ish uchun bufferlar
    output_buffer = io.StringIO()
    error_buffer = io.StringIO()
    
    try:
        # Standart chiqish va xatolarni o'zgaruvchilarga yo'naltirish
        with contextlib.redirect_stdout(output_buffer), \
             contextlib.redirect_stderr(error_buffer):
            
            # Global muhitni sozlash
            safe_globals = {**globals(), **SAFE_BUILTINS}
            safe_locals = {}
            
            # Kerakli modullarni import qilish
            for module_name in ALLOWED_MODULES:
                try:
                    safe_globals[module_name] = importlib.import_module(module_name)
                except ImportError:
                    pass
            
            # Kodni ishga tushirish
            exec(code, safe_globals, safe_locals)
            
            # Agar kodda hech narsa chiqmasa, xabar qaytarish
            output = output_buffer.getvalue()
            if not output.strip():
                return "Kod muvaffaqiyatli bajarildi, lekin hech qanday chiqish yo'q."
            return output
            
    except Exception as e:
        # Xatolik haqida tushunarli xabar qaytarish
        error_type = type(e).__name__
        error_msg = str(e)
        traceback_str = '\n'.join(traceback.format_exception_only(type(e), e))
        return f"Xato ({error_type}): {error_msg}\n\nTafsilotlar:\n{traceback_str}"

# Asosiy sahifa uchun view
def index(request):
    # Agar POST so'rovi kelsa (ya'ni foydalanuvchi kod yuborgan bo'lsa)
    if request.method == "POST":
        code = request.POST.get('code', '').strip()
        
        # Agar kod bo'sh bo'lsa
        if not code:
            return render(request, 'index.html', {
                'code': '',
                'output': 'Iltimos, biron bir kod yozing.'
            })
        
        # Kodni tekshirish
        is_safe, error_message = check_restricted_code(code)
        if not is_safe:
            return render(request, 'index.html', {
                'code': code,
                'output': f"Xavfsizlik xatosi: {error_message}"
            })
        
        # Kodni ishga tushirish
        output = execute_code(code)
        
        return render(request, 'index.html', {
            'code': code,
            'output': output
        })
    
    # Agar oddiy GET so'rovi bo'lsa, bo'sh shablonni qaytarish
    return render(request, 'index.html', {
        'code': '# Python kodlaringizni shu yerga yozing\nprint("Salom, Dunyo!")',
        'output': 'Natija shu yerda ko\'rinadi...'
    })