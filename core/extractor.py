
import re
import os
import time
from typing import List, Tuple
from ..config import Config

class CodeExtractor:
    """Extracts and manages code blocks from AI responses"""
    
    @staticmethod
    def extract_code_blocks(text: str) -> List[Tuple[str, str]]:
        """
        Extract code blocks from markdown text.
        Returns list of tuples: (language, code)
        """
        code_blocks = []
        
        # Pattern explanation:
        # ```([\w\-\+#]*)? - optional language identifier
        # \s* - optional whitespace/newline
        # (.*?) - non-greedy capture of code content
        # ``` - closing backticks
        pattern = r'```([\w\-\+#]*)\s*\n(.*?)\n```'
        
        matches = re.finditer(pattern, text, re.DOTALL | re.MULTILINE)
        
        for match in matches:
            lang = match.group(1).strip() if match.group(1) else "text"
            code = match.group(2)
            
            code_lines = code.split('\n')
            
            # Remove empty lines from start
            while code_lines and not code_lines[0].strip():
                code_lines.pop(0)
            
            # Remove empty lines from end
            while code_lines and not code_lines[-1].strip():
                code_lines.pop()
            
            code = '\n'.join(code_lines)
            
            if code.strip():
                code_blocks.append((lang, code))
        
        return code_blocks
    
    @staticmethod
    def save_code_block(code: str, language: str, index: int = 0) -> str:
        """Save a code block to file and return the path"""
        os.makedirs(Config.CODE_OUTPUT_DIR, exist_ok=True)
        
        # Determine file extension
        ext_map = {
            "python": "py", "javascript": "js", "typescript": "ts",
            "java": "java", "cpp": "cpp", "c++": "cpp", "c": "c", "csharp": "cs", "c#": "cs",
            "go": "go", "rust": "rs", "php": "php", "ruby": "rb",
            "swift": "swift", "kotlin": "kt", "html": "html", "css": "css",
            "sql": "sql", "bash": "sh", "shell": "sh", "powershell": "ps1",
            "perl": "pl", "scala": "scala", "r": "r", "matlab": "m",
            "json": "json", "xml": "xml", "yaml": "yml", "yml": "yml",
            "markdown": "md", "md": "md", "text": "txt", "txt": "txt"
        }
        ext = ext_map.get(language.lower(), "txt")
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"code_{timestamp}_{index+1}.{ext}"
        filepath = os.path.join(Config.CODE_OUTPUT_DIR, filename)
        
        try:
            with open(filepath, 'w', encoding='utf-8', newline='') as f:
                f.write(code)
                f.flush()
                os.fsync(f.fileno())
        except Exception as e:
            raise Exception(f"Failed to save code block: {e}")
        
        return filepath
