# Language Selection, source: https://github.com/bigcode-project/bigcode-dataset/blob/main/language_selection/programming-languages-to-file-extensions.json  # noqa E501
from typing import Dict

language_extension_map_org = {"ABAP": [".abap"], "AGS Script": [".ash"], "AMPL": [".ampl"], "ANTLR": [".g4"], "API Blueprint": [".apib"], "APL": [".apl", ".dyalog"], "ASP": [".asp", ".asax", ".ascx", ".ashx", ".asmx", ".aspx", ".axd"], "ATS": [".dats", ".hats", ".sats"], "ActionScript": [".as"], "Ada": [".adb", ".ada", ".ads"], "Agda": [".agda"], "Alloy": [".als"], "ApacheConf": [".apacheconf", ".vhost"], "AppleScript": [".applescript", ".scpt"], "Arc": [".arc"], "Arduino": [".ino"], "AsciiDoc": [".asciidoc", ".adoc"], "AspectJ": [".aj"], "Assembly": [".asm", ".a51", ".nasm"], "Augeas": [".aug"], "AutoHotkey": [".ahk", ".ahkl"], "AutoIt": [".au3"], "Awk": [".awk", ".auk", ".gawk", ".mawk", ".nawk"], "Batchfile": [".bat", ".cmd"], "Befunge": [".befunge"], "Bison": [".bison"], "BitBake": [".bb"], "BlitzBasic": [".decls"], "BlitzMax": [".bmx"], "Bluespec": [".bsv"], "Boo": [".boo"], "Brainfuck": [".bf"], "Brightscript": [".brs"], "Bro": [".bro"], "C": [".c", ".cats", ".h", ".idc", ".w"], "C#": [".cs", ".cake", ".cshtml", ".csx"], "C++": [".cpp", ".c++", ".cc", ".cp", ".cxx", ".h++", ".hh", ".hpp", ".hxx", ".inl", ".ipp", ".tcc", ".tpp", ".C", ".H"], "C-ObjDump": [".c-objdump"], "C2hs Haskell": [".chs"], "CLIPS": [".clp"], "CMake": [".cmake", ".cmake.in"], "COBOL": [".cob", ".cbl", ".ccp", ".cobol", ".cpy"], "CSS": [".css"], "CSV": [".csv"], "Cap'n Proto": [".capnp"], "CartoCSS": [".mss"], "Ceylon": [".ceylon"], "Chapel": [".chpl"], "ChucK": [".ck"], "Cirru": [".cirru"], "Clarion": [".clw"], "Clean": [".icl", ".dcl"], "Click": [".click"], "Clojure": [".clj", ".boot", ".cl2", ".cljc", ".cljs", ".cljs.hl", ".cljscm", ".cljx", ".hic"], "CoffeeScript": [".coffee", "._coffee", ".cjsx", ".cson", ".iced"], "ColdFusion": [".cfm", ".cfml"], "ColdFusion CFC": [".cfc"], "Common Lisp": [".lisp", ".asd", ".lsp", ".ny", ".podsl", ".sexp"], "Component Pascal": [".cps"], "Coq": [".coq"], "Cpp-ObjDump": [".cppobjdump", ".c++-objdump", ".c++objdump", ".cpp-objdump", ".cxx-objdump"], "Creole": [".creole"], "Crystal": [".cr"], "Csound": [".csd"], "Cucumber": [".feature"], "Cuda": [".cu", ".cuh"], "Cycript": [".cy"], "Cython": [".pyx", ".pxd", ".pxi"], "D": [".di"], "D-ObjDump": [".d-objdump"], "DIGITAL Command Language": [".com"], "DM": [".dm"], "DNS Zone": [".zone", ".arpa"], "Darcs Patch": [".darcspatch", ".dpatch"], "Dart": [".dart"], "Diff": [".diff", ".patch"], "Dockerfile": [".dockerfile", "Dockerfile"], "Dogescript": [".djs"], "Dylan": [".dylan", ".dyl", ".intr", ".lid"], "E": [".E"], "ECL": [".ecl", ".eclxml"], "Eagle": [".sch", ".brd"], "Ecere Projects": [".epj"], "Eiffel": [".e"], "Elixir": [".ex", ".exs"], "Elm": [".elm"], "Emacs Lisp": [".el", ".emacs", ".emacs.desktop"], "EmberScript": [".em", ".emberscript"], "Erlang": [".erl", ".escript", ".hrl", ".xrl", ".yrl"], "F#": [".fs", ".fsi", ".fsx"], "FLUX": [".flux"], "FORTRAN": [".f90", ".f", ".f03", ".f08", ".f77", ".f95", ".for", ".fpp"], "Factor": [".factor"], "Fancy": [".fy", ".fancypack"], "Fantom": [".fan"], "Formatted": [".eam.fs"], "Forth": [".fth", ".4th", ".forth", ".frt"], "FreeMarker": [".ftl"], "G-code": [".g", ".gco", ".gcode"], "GAMS": [".gms"], "GAP": [".gap", ".gi"], "GAS": [".s"], "GDScript": [".gd"], "GLSL": [".glsl", ".fp", ".frag", ".frg", ".fsh", ".fshader", ".geo", ".geom", ".glslv", ".gshader", ".shader", ".vert", ".vrx", ".vsh", ".vshader"], "Genshi": [".kid"], "Gentoo Ebuild": [".ebuild"], "Gentoo Eclass": [".eclass"], "Gettext Catalog": [".po", ".pot"], "Glyph": [".glf"], "Gnuplot": [".gp", ".gnu", ".gnuplot", ".plot", ".plt"], "Go": [".go"], "Golo": [".golo"], "Gosu": [".gst", ".gsx", ".vark"], "Grace": [".grace"], "Gradle": [".gradle"], "Grammatical Framework": [".gf"], "GraphQL": [".graphql"], "Graphviz (DOT)": [".dot", ".gv"], "Groff": [".man", ".1", ".1in", ".1m", ".1x", ".2", ".3", ".3in", ".3m", ".3qt", ".3x", ".4", ".5", ".6", ".7", ".8", ".9", ".me", ".rno", ".roff"], "Groovy": [".groovy", ".grt", ".gtpl", ".gvy"], "Groovy Server Pages": [".gsp"], "HCL": [".hcl", ".tf"], "HLSL": [".hlsl", ".fxh", ".hlsli"], "HTML": [".html", ".htm", ".html.hl", ".xht", ".xhtml"], "HTML+Django": [".mustache", ".jinja"], "HTML+EEX": [".eex"], "HTML+ERB": [".erb", ".erb.deface"], "HTML+PHP": [".phtml"], "HTTP": [".http"], "Haml": [".haml", ".haml.deface"], "Handlebars": [".handlebars", ".hbs"], "Harbour": [".hb"], "Haskell": [".hs", ".hsc"], "Haxe": [".hx", ".hxsl"], "Hy": [".hy"], "IDL": [".dlm"], "IGOR Pro": [".ipf"], "INI": [".ini", ".cfg", ".prefs", ".properties"], "IRC log": [".irclog", ".weechatlog"], "Idris": [".idr", ".lidr"], "Inform 7": [".ni", ".i7x"], "Inno Setup": [".iss"], "Io": [".io"], "Ioke": [".ik"], "Isabelle": [".thy"], "J": [".ijs"], "JFlex": [".flex", ".jflex"], "JSON": [".json", ".geojson", ".lock", ".topojson"], "JSON5": [".json5"], "JSONLD": [".jsonld"], "JSONiq": [".jq"], "JSX": [".jsx"], "Jade": [".jade"], "Jasmin": [".j"], "Java": [".java"], "Java Server Pages": [".jsp"], "JavaScript": [".js", "._js", ".bones", ".es6", ".jake", ".jsb", ".jscad", ".jsfl", ".jsm", ".jss", ".njs", ".pac", ".sjs", ".ssjs", ".xsjs", ".xsjslib"], "Julia": [".jl"], "Jupyter Notebook": [".ipynb"], "KRL": [".krl"], "KiCad": [".kicad_pcb"], "Kit": [".kit"], "Kotlin": [".kt", ".ktm", ".kts"], "LFE": [".lfe"], "LLVM": [".ll"], "LOLCODE": [".lol"], "LSL": [".lsl", ".lslp"], "LabVIEW": [".lvproj"], "Lasso": [".lasso", ".las", ".lasso8", ".lasso9", ".ldml"], "Latte": [".latte"], "Lean": [".lean", ".hlean"], "Less": [".less"], "Lex": [".lex"], "LilyPond": [".ly", ".ily"], "Linker Script": [".ld", ".lds"], "Liquid": [".liquid"], "Literate Agda": [".lagda"], "Literate CoffeeScript": [".litcoffee"], "Literate Haskell": [".lhs"], "LiveScript": [".ls", "._ls"], "Logos": [".xm", ".x", ".xi"], "Logtalk": [".lgt", ".logtalk"], "LookML": [".lookml"], "Lua": [".lua", ".nse", ".pd_lua", ".rbxs", ".wlua"], "M": [".mumps"], "M4": [".m4"], "MAXScript": [".mcr"], "MTML": [".mtml"], "MUF": [".muf"], "Makefile": [".mak", ".mk", ".mkfile", "Makefile"], "Mako": [".mako", ".mao"], "Maple": [".mpl"], "Markdown": [".md", ".markdown", ".mkd", ".mkdn", ".mkdown", ".ron"], "Mask": [".mask"], "Mathematica": [".mathematica", ".cdf", ".ma", ".mt", ".nb", ".nbp", ".wl", ".wlt"], "Matlab": [".matlab"], "Max": [".maxpat", ".maxhelp", ".maxproj", ".mxt", ".pat"], "MediaWiki": [".mediawiki", ".wiki"], "Metal": [".metal"], "MiniD": [".minid"], "Mirah": [".druby", ".duby", ".mir", ".mirah"], "Modelica": [".mo"], "Module Management System": [".mms", ".mmk"], "Monkey": [".monkey"], "MoonScript": [".moon"], "Myghty": [".myt"], "NSIS": [".nsi", ".nsh"], "NetLinx": [".axs", ".axi"], "NetLinx+ERB": [".axs.erb", ".axi.erb"], "NetLogo": [".nlogo"], "Nginx": [".nginxconf"], "Nimrod": [".nim", ".nimrod"], "Ninja": [".ninja"], "Nit": [".nit"], "Nix": [".nix"], "Nu": [".nu"], "NumPy": [".numpy", ".numpyw", ".numsc"], "OCaml": [".ml", ".eliom", ".eliomi", ".ml4", ".mli", ".mll", ".mly"], "ObjDump": [".objdump"], "Objective-C++": [".mm"], "Objective-J": [".sj"], "Octave": [".oct"], "Omgrofl": [".omgrofl"], "Opa": [".opa"], "Opal": [".opal"], "OpenCL": [".cl", ".opencl"], "OpenEdge ABL": [".p"], "OpenSCAD": [".scad"], "Org": [".org"], "Ox": [".ox", ".oxh", ".oxo"], "Oxygene": [".oxygene"], "Oz": [".oz"], "PAWN": [".pwn"], "PHP": [".php", ".aw", ".ctp", ".php3", ".php4", ".php5", ".phps", ".phpt"], "POV-Ray SDL": [".pov"], "Pan": [".pan"], "Papyrus": [".psc"], "Parrot": [".parrot"], "Parrot Assembly": [".pasm"], "Parrot Internal Representation": [".pir"], "Pascal": [".pas", ".dfm", ".dpr", ".lpr"], "Perl": [".pl", ".al", ".perl", ".ph", ".plx", ".pm", ".psgi", ".t"], "Perl6": [".6pl", ".6pm", ".nqp", ".p6", ".p6l", ".p6m", ".pl6", ".pm6"], "Pickle": [".pkl"], "PigLatin": [".pig"], "Pike": [".pike", ".pmod"], "Pod": [".pod"], "PogoScript": [".pogo"], "Pony": [".pony"], "PostScript": [".ps", ".eps"], "PowerShell": [".ps1", ".psd1", ".psm1"], "Processing": [".pde"], "Prolog": [".prolog", ".yap"], "Propeller Spin": [".spin"], "Protocol Buffer": [".proto"], "Public Key": [".pub"], "Pure Data": [".pd"], "PureBasic": [".pb", ".pbi"], "PureScript": [".purs"], "Python": [".py", ".bzl", ".gyp", ".lmi", ".pyde", ".pyp", ".pyt", ".pyw", ".tac", ".wsgi", ".xpy"], "Python traceback": [".pytb"], "QML": [".qml", ".qbs"], "QMake": [".pri"], "R": [".r", ".rd", ".rsx"], "RAML": [".raml"], "RDoc": [".rdoc"], "REALbasic": [".rbbas", ".rbfrm", ".rbmnu", ".rbres", ".rbtbar", ".rbuistate"], "RHTML": [".rhtml"], "RMarkdown": [".rmd"], "Racket": [".rkt", ".rktd", ".rktl", ".scrbl"], "Ragel in Ruby Host": [".rl"], "Raw token data": [".raw"], "Rebol": [".reb", ".r2", ".r3", ".rebol"], "Red": [".red", ".reds"], "Redcode": [".cw"], "Ren'Py": [".rpy"], "RenderScript": [".rsh"], "RobotFramework": [".robot"], "Rouge": [".rg"], "Ruby": [".rb", ".builder", ".gemspec", ".god", ".irbrc", ".jbuilder", ".mspec", ".podspec", ".rabl", ".rake", ".rbuild", ".rbw", ".rbx", ".ru", ".ruby", ".thor", ".watchr"], "Rust": [".rs", ".rs.in"], "SAS": [".sas"], "SCSS": [".scss"], "SMT": [".smt2", ".smt"], "SPARQL": [".sparql", ".rq"], "SQF": [".sqf", ".hqf"], "SQL": [".pls", ".pck", ".pkb", ".pks", ".plb", ".plsql", ".sql", ".cql", ".ddl", ".prc", ".tab", ".udf", ".viw", ".db2"], "STON": [".ston"], "SVG": [".svg"], "Sage": [".sage", ".sagews"], "SaltStack": [".sls"], "Sass": [".sass"], "Scala": [".scala", ".sbt"], "Scaml": [".scaml"], "Scheme": [".scm", ".sld", ".sps", ".ss"], "Scilab": [".sci", ".sce"], "Self": [".self"], "Shell": [".sh", ".bash", ".bats", ".command", ".ksh", ".sh.in", ".tmux", ".tool", ".zsh"], "ShellSession": [".sh-session"], "Shen": [".shen"], "Slash": [".sl"], "Slim": [".slim"], "Smali": [".smali"], "Smalltalk": [".st"], "Smarty": [".tpl"], "Solidity": [".sol"], "SourcePawn": [".sp", ".sma"], "Squirrel": [".nut"], "Stan": [".stan"], "Standard ML": [".ML", ".fun", ".sig", ".sml"], "Stata": [".do", ".ado", ".doh", ".ihlp", ".mata", ".matah", ".sthlp"], "Stylus": [".styl"], "SuperCollider": [".scd"], "Swift": [".swift"], "SystemVerilog": [".sv", ".svh", ".vh"], "TOML": [".toml"], "TXL": [".txl"], "Tcl": [".tcl", ".adp", ".tm"], "Tcsh": [".tcsh", ".csh"], "TeX": [".tex", ".aux", ".bbx", ".bib", ".cbx", ".dtx", ".ins", ".lbx", ".ltx", ".mkii", ".mkiv", ".mkvi", ".sty", ".toc"], "Tea": [".tea"], "Text": [".txt", ".no"], "Textile": [".textile"], "Thrift": [".thrift"], "Turing": [".tu"], "Turtle": [".ttl"], "Twig": [".twig"], "TypeScript": [".ts", ".tsx"], "Unified Parallel C": [".upc"], "Unity3D Asset": [".anim", ".asset", ".mat", ".meta", ".prefab", ".unity"], "Uno": [".uno"], "UnrealScript": [".uc"], "UrWeb": [".ur", ".urs"], "VCL": [".vcl"], "VHDL": [".vhdl", ".vhd", ".vhf", ".vhi", ".vho", ".vhs", ".vht", ".vhw"], "Vala": [".vala", ".vapi"], "Verilog": [".veo"], "VimL": [".vim"], "Visual Basic": [".vb", ".bas", ".frm", ".frx", ".vba", ".vbhtml", ".vbs"], "Volt": [".volt"], "Vue": [".vue"], "Web Ontology Language": [".owl"], "WebAssembly": [".wat"], "WebIDL": [".webidl"], "X10": [".x10"], "XC": [".xc"], "XML": [".xml", ".ant", ".axml", ".ccxml", ".clixml", ".cproject", ".csl", ".csproj", ".ct", ".dita", ".ditamap", ".ditaval", ".dll.config", ".dotsettings", ".filters", ".fsproj", ".fxml", ".glade", ".grxml", ".iml", ".ivy", ".jelly", ".jsproj", ".kml", ".launch", ".mdpolicy", ".mxml", ".nproj", ".nuspec", ".odd", ".osm", ".plist", ".props", ".ps1xml", ".psc1", ".pt", ".rdf", ".rss", ".scxml", ".srdf", ".storyboard", ".stTheme", ".sublime-snippet", ".targets", ".tmCommand", ".tml", ".tmLanguage", ".tmPreferences", ".tmSnippet", ".tmTheme", ".ui", ".urdf", ".ux", ".vbproj", ".vcxproj", ".vssettings", ".vxml", ".wsdl", ".wsf", ".wxi", ".wxl", ".wxs", ".x3d", ".xacro", ".xaml", ".xib", ".xlf", ".xliff", ".xmi", ".xml.dist", ".xproj", ".xsd", ".xul", ".zcml"], "XPages": [".xsp-config", ".xsp.metadata"], "XProc": [".xpl", ".xproc"], "XQuery": [".xquery", ".xq", ".xql", ".xqm", ".xqy"], "XS": [".xs"], "XSLT": [".xslt", ".xsl"], "Xojo": [".xojo_code", ".xojo_menu", ".xojo_report", ".xojo_script", ".xojo_toolbar", ".xojo_window"], "Xtend": [".xtend"], "YAML": [".yml", ".reek", ".rviz", ".sublime-syntax", ".syntax", ".yaml", ".yaml-tmlanguage"], "YANG": [".yang"], "Yacc": [".y", ".yacc", ".yy"], "Zephir": [".zep"], "Zig": [".zig"], "Zimpl": [".zimpl", ".zmpl", ".zpl"], "desktop": [".desktop", ".desktop.in"], "eC": [".ec", ".eh"], "edn": [".edn"], "fish": [".fish"], "mupad": [".mu"], "nesC": [".nc"], "ooc": [".ooc"], "reStructuredText": [".rst", ".rest", ".rest.txt", ".rst.txt"], "wisp": [".wisp"], "xBase": [".prg", ".prw"]}  # noqa E501
language_extension_map = {k.lower(): v for k, v in language_extension_map_org.items()}

# Bad Extensions, source: https://github.com/EleutherAI/github-downloader/blob/345e7c4cbb9e0dc8a0615fd995a08bf9d73b3fe6/download_repo_text.py  # noqa: E501
bad_extensions = [
    'app',
    'bin',
    'bmp',
    'bz2',
    'class',
    'csv',
    'dat',
    'db',
    'dll',
    'dylib',
    'egg',
    'eot',
    'exe',
    'gif',
    'gitignore',
    'glif',
    'gradle',
    'gz',
    'ico',
    'jar',
    'jpeg',
    'jpg',
    'lo',
    'lock',
    'log',
    'mp3',
    'mp4',
    'nar',
    'o',
    'ogg',
    'otf',
    'p',
    'pdf',
    'png',
    'pickle',
    'pkl',
    'pyc',
    'pyd',
    'pyo',
    'rkt',
    'so',
    'ss',
    'svg',
    'tar',
    'tsv',
    'ttf',
    'war',
    'webm',
    'woff',
    'woff2',
    'xz',
    'zip',
    'zst',
    'snap'
]


def filter_bad_extensions(files):
    return [f for f in files if is_valid_file(f.filename)]


def is_valid_file(filename):
    return filename.split('.')[-1] not in bad_extensions


def sort_files_by_main_languages(languages: Dict, files: list):
    """
    Sort files by their main language, put the files that are in the main language first and the rest files after
    """
    # sort languages by their size
    languages_sorted_list = [k for k, v in sorted(languages.items(), key=lambda item: item[1], reverse=True)]
    # languages_sorted = sorted(languages, key=lambda x: x[1], reverse=True)
    # get all extensions for the languages
    main_extensions = []
    for language in languages_sorted_list:
        if language.lower() in language_extension_map:
            main_extensions.append(language_extension_map[language.lower()])
        else:
            main_extensions.append([])

    # filter out files bad extensions
    files_filtered = filter_bad_extensions(files)
    # sort files by their extension, put the files that are in the main extension first
    # and the rest files after, map languages_sorted to their respective files
    files_sorted = []
    rest_files = {}

    main_extensions_flat = []
    for ext in main_extensions:
        main_extensions_flat.extend(ext)

    for extensions, lang in zip(main_extensions, languages_sorted_list):  # noqa: B905
        tmp = []
        for file in files_filtered:
            extension_str = f".{file.filename.split('.')[-1]}"
            if extension_str in extensions:
                tmp.append(file)
            else:
                if (file.filename not in rest_files) and (extension_str not in main_extensions_flat):
                    rest_files[file.filename] = file
        if len(tmp) > 0:
            files_sorted.append({"language": lang, "files": tmp})
    files_sorted.append({"language": "Other", "files": list(rest_files.values())})
    return files_sorted
