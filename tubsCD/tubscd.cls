% ========================================================================================
%        ________  __   ____                                   __                 _      
%       /_  __/ / / /  / __ )_________ ___  ______  __________/ /_ _      _____  (_)___ _
%        / / / / / /  / __  / ___/ __ `/ / / / __ \/ ___/ ___/ __ \ | /| / / _ \/ / __ `/
%       / / / /_/ /  / /_/ / /  / /_/ / /_/ / / / (__  ) /__/ / / / |/ |/ /  __/ / /_/ / 
%      /_/  \____/  /_____/_/   \__,_/\__,_/_/ /_/____/\___/_/ /_/|__/|__/\___/_/\__, /  
%     __        ______    _  __    __________     _    __           __          /____/   
%    / /  ____ /_  __/__ | |/ /   / ____/ __ \   | |  / /___  _____/ /___ _____ ____     
%   / /  / __ `// / / _ \|   /   / /   / / / /   | | / / __ \/ ___/ / __ `/ __ `/ _ \    
%  / /__/ /_/ // / /  __/   |   / /___/ /_/ /    | |/ / /_/ / /  / / /_/ / /_/ /  __/    
% /_____|__,_//_/  \___/_/|_|   \____/_____/     |___/\____/_/  /_/\__,_/\__, /\___/     
%                                                                       /____/
%
% =======================================================================================
%
% This is the main file of the corporate design.
% In here, all aspects of the cd-toolbox
% (available at https://www.tu-braunschweig.de/presse/corporate-design/cd-toolbox )
% are brought together to be available in every project that uses the class tubscd.
% However, the tubscd class does not inherently force its settings on the user.
% More precicely, it offers options that can be invoked, and if called, adhere to
% the corporate design of the technical university of brunswick.
%
% For help you can reach out to tubs-latex@tu-braunschweig.de and
% bug reporting can be done at https://git.rz.tu-bs.de/v.hille/tubs-latex-cd-lite
%
% ===================================================================================
% Version Numbering:

\def\tubscdVersion{1.1}%
\def\tubscdDate{2025/09/18}%

% ===================================
% Identification:

% define class format (latex requirement)
\NeedsTeXFormat{LaTeX2e}[1999/12/01]%
% say which class this document creates
\ProvidesClass{tubsCD/tubscd}[\tubscdDate~\tubscdVersion]%

% for decision handeling
\RequirePackage{etoolbox}%

% ===================================
% Define class macro

\RequirePackage{kvoptions}%
\SetupKeyvalOptions{%
    family = tubs,%
    prefix = tubs@,%
    setkeys = \setkeys%
}%

% ===================================
% When calling the class tubscd, one can send additional options.
% The default values, as well as all other options are defined and processed here

\DeclareStringOption[scrbook]{basedocumentclass} % any supported documentclass, hopefully
\DeclareStringOption[nexus]{font} %arial, tnr, other (no guarantee)
\DeclareStringOption[a4paper]{papersize} %common A norms, langpaper
\DeclareStringOption[11]{fontsize} %fontsize for normal text
\DeclareStringOption[0]{bindingoffset} %define binding offset in mm
\DeclareStringOption[oneside]{sideoption} %twoside
\DeclareStringOption[portrait]{paperformat} %landscape
%\DeclareStringOption[off]{specialformat} %poster, custom
\DeclareStringOption[fullpage]{redDivisionLine} %skipborder, off
\DeclareStringOption[topleft]{tubanner} %topright, bottomleft, bottomright, off
\DeclareStringOption[off]{template} %all template names
\DeclareStringOption[german]{language} %should support all babel languages
\ProcessKeyvalOptions*

% ===================================
% Some light bug fixing

% The following removes the DIV warning, which appears for big paper sizes with small
% text size. But because this is both defined in the corporate design, it is a feature,
% and the warning should be ignored
\RequirePackage{silence}%
\WarningFilter{typearea}{Very low DIV value!}%
\WarningFilter{typearea}{Bad type area settings!}%

% The base class on which tubscd is defined on top must be loaded somewhere in this area.
% This is because it needs tubs@papersize and because it must be loaded in the main
% class file to ensure \pagewidth works propperly.
% unfortunately, the side option  cannot be defined dynamically and thus we need the if case construction
\ifdefstring{\tubs@sideoption}{oneside}{%
    \LoadClass[\tubs@papersize, oneside, fontsize=\tubs@fontsize pt]{\tubs@basedocumentclass}%
}{%
    \LoadClass[\tubs@papersize, twoside, fontsize=\tubs@fontsize pt]{\tubs@basedocumentclass}%
}%

% ===================================
% Load coorporate design settings:
% The packages that are required for the class files to work, are loaded here redundantly
% to give a better overview of the used packages. This is helpful in avoiding using
% similar packages when the feature can already be used with similar syntax.

% Fonts:
\RequirePackage{fontspec} % must be loaded after \LoadClass
\RequirePackage{lmodern}
\RequirePackage{tubsCD/cdFonts}
% Coloring:
\RequirePackage{xcolor}
\RequirePackage{tubsCD/cdColors}
% TU Banner:
\RequirePackage{xkeyval}
\RequirePackage{pgf} % for sum formula
\RequirePackage{tubsCD/cdTUBanner}
% Senderspace:
\RequirePackage{tubsCD/cdSenderspace}
% Special Page (Gauss) Layout:
\RequirePackage{tikz} % drawing and positioning objects
\usetikzlibrary{calc} % Required for coordinate calculations
\RequirePackage{xstring} % string matching and editing
\RequirePackage{ifthen} % logic
\RequirePackage{tubsCD/cdGaussianLayout}
% Special Page (Module) Layout:
\RequirePackage{tubsCD/cdModuleLayout}

% ===================================
% Document Layout:

% unfortunately, landscape cannot be defined dynamically and thus we need the if case construction
\ifdefstring{\tubs@paperformat}{landscape}{%
    \RequirePackage[\tubs@papersize,landscape=true, includehead, includefoot]{geometry}
}{%
    \RequirePackage[\tubs@papersize,landscape=false, includehead, includefoot]{geometry}
}%

% load languages:
\usepackage[\tubs@language]{babel}

% Load Templates:
\RequirePackage{tubsCD/cdTemplateLoader}
