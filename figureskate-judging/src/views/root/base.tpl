<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>FigureSkatingJudginh</title>
    <link href="/css/base.css" rel="stylesheet" type="text/css">
    % for css_file in css_files:
    <link href="{{css_file}}" rel="stylesheet" type="text/css">
    % end
  </head>
<body>
<div id="wrapper">
  <div id="header">
    <h1>FigureSkatingJudge</h1>
    <p>フィギュアスケート採点システム</p>
  </div>
  <div id="nav">
    <ul>
      <li><a class="active" href="#">HOME</a></li>
      <li><a href="#">ABOUT</a></li>
      <li><a href="#">CONTACT</a></li>
    </ul>
  </div>
  <div id="container">
    % # import main contents.
    % include('%s' % (tpl_func_file), contents=main_contents)
  </div>
  <div id="footer">
    <p>&copy; Pyohei. All right reserved.</p>
  </div>
</div>
</body>
</html>
