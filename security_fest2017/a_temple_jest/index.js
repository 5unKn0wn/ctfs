var express = require(&#39;express&#39;);
var request = require(&#34;request&#34;);
var eval = require(&#34;eval&#34;);
var ejs = require(&#39;ejs&#39;);
var app = express();
var spawn = spawn = require(&#39;threads&#39;).spawn;

var bodyParser = require(&#39;body-parser&#39;);
app.use(bodyParser.urlencoded({
	extended: true
}));


app.listen(3003, function () {
  console.log(&#39;A temple jest app listening on port 3003!&#39;)
});

app.get(&#39;/render/:name&#39;, function (req, res, next) {
  console.log(req.originalUrl);
  var thread = spawn(function(input, done) {
    var ejs = require(&#39;ejs&#39;);
    flag = &#34;SCTF{m3m0ry_l34k_Schm3m0ry_l34k}&#34;
    var html = ejs.render(&#34;&lt;%= &#34;+input.name+&#34; %&gt; is under construction...&lt;%# &#34;+(&#34;---&#34;+flag).repeat(20)+&#34; %&gt;&#34;, {});
    done(html);
  });

  //Hack to avoid for(;;){} hanging the whole server...
  setTimeout(function(){thread.kill();try{res.send(&#34;timeout&#34;);}catch(z){}}, 3000);
  thread.send({&#34;name&#34;: req.params.name, flag: &#34;&#34;}).on(&#34;message&#34;, function(html){res.send(html)});
});

app.get(&#39;/&#39;, function(req, res, next){
  return ejs.renderFile(&#39;./templates/index.ejs&#39;, function(err, data){res.send(data);});
});

app.get(&#39;/package.json&#39;, function(req, res, next){
  res.sendfile(&#39;./package.json&#39;);
});
 is under construction...