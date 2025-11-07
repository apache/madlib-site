var NAVTREE =
[
  [ "MADlib", "index.html", [
    [ "Main Page", "index.html", null ],
    [ "Modules", "modules.html", [
      [ "Data Modeling", "group__grp__modeling.html", [
        [ "Supervised Learning", "group__grp__suplearn.html", [
          [ "Naive Bayes Classification", "group__grp__bayes.html", null ],
          [ "Linear Regression", "group__grp__linreg.html", null ],
          [ "Logistic Regression", "group__grp__logreg.html", null ],
          [ "Multinomial Logistic Regression", "group__grp__mlogreg.html", null ],
          [ "Cross Validation", "group__grp__validation.html", null ],
          [ "Elastic Net Regularization", "group__grp__elasticnet.html", null ],
          [ "Decision Tree", "group__grp__dectree.html", null ],
          [ "Random Forest", "group__grp__rf.html", null ],
          [ "Linear Support Vector Machines", "group__grp__linear__svm.html", null ],
          [ "Support Vector Machines", "group__grp__kernmach.html", null ],
          [ "Cox-Proportional Hazards Regression", "group__grp__cox__prop__hazards.html", null ],
          [ "Conditional Random Field", "group__grp__crf.html", null ]
        ] ],
        [ "Unsupervised Learning", "group__grp__unsuplearn.html", [
          [ "Association Rules", "group__grp__assoc__rules.html", null ],
          [ "k-Means Clustering", "group__grp__kmeans.html", null ],
          [ "Low-rank Matrix Factorization", "group__grp__lmf.html", null ],
          [ "SVD Matrix Factorisation", "group__grp__svdmf.html", null ],
          [ "Latent Dirichlet Allocation", "group__grp__lda.html", null ]
        ] ]
      ] ],
      [ "Descriptive Statistics", "group__grp__desc__stats.html", [
        [ "Sketch-based Estimators", "group__grp__sketches.html", [
          [ "CountMin (Cormode-Muthukrishnan)", "group__grp__countmin.html", null ],
          [ "FM (Flajolet-Martin)", "group__grp__fmsketch.html", null ],
          [ "MFV (Most Frequent Values)", "group__grp__mfvsketch.html", null ]
        ] ],
        [ "Profile", "group__grp__profile.html", null ],
        [ "Summary", "group__grp__summary.html", null ],
        [ "Pearson's correlation", "group__grp__correlation.html", null ],
        [ "Quantile", "group__grp__quantile.html", null ]
      ] ],
      [ "Inferential Statistics", "group__grp__stats.html", [
        [ "Hypothesis Tests", "group__grp__stats__tests.html", null ]
      ] ],
      [ "Support Modules", "group__grp__support.html", [
        [ "Array Operations", "group__grp__array.html", null ],
        [ "Conjugate Gradient", "group__grp__cg.html", null ],
        [ "Linear-Algebra Operations", "group__grp__linalg.html", null ],
        [ "Sparse Vectors", "group__grp__svec.html", null ],
        [ "Probability Functions", "group__grp__prob.html", null ],
        [ "Random Sampling", "group__grp__sample.html", null ],
        [ "Compatibility", "group__grp__compatibility.html", null ],
        [ "DB Administrator Utilities", "group__grp__utilities.html", null ]
      ] ]
    ] ],
    [ "File List", "files.html", [
      [ "array_ops.sql_in", "array__ops_8sql__in.html", null ],
      [ "assoc_rules.sql_in", "assoc__rules_8sql__in.html", null ],
      [ "bayes.sql_in", "bayes_8sql__in.html", null ],
      [ "c45.sql_in", "c45_8sql__in.html", null ],
      [ "compatibility.sql_in", "compatibility_8sql__in.html", null ],
      [ "conjugate_gradient.sql_in", "conjugate__gradient_8sql__in.html", null ],
      [ "correlation.sql_in", "correlation_8sql__in.html", null ],
      [ "cox_prop_hazards.sql_in", "cox__prop__hazards_8sql__in.html", null ],
      [ "crf.sql_in", "crf_8sql__in.html", null ],
      [ "crf_data_loader.sql_in", "crf__data__loader_8sql__in.html", null ],
      [ "crf_feature_gen.sql_in", "crf__feature__gen_8sql__in.html", null ],
      [ "cross_validation.sql_in", "cross__validation_8sql__in.html", null ],
      [ "dt.sql_in", "dt_8sql__in.html", null ],
      [ "dt_preproc.sql_in", "dt__preproc_8sql__in.html", null ],
      [ "dt_utility.sql_in", "dt__utility_8sql__in.html", null ],
      [ "elastic_net.sql_in", "elastic__net_8sql__in.html", null ],
      [ "hypothesis_tests.sql_in", "hypothesis__tests_8sql__in.html", null ],
      [ "kmeans.sql_in", "kmeans_8sql__in.html", null ],
      [ "lda.sql_in", "lda_8sql__in.html", null ],
      [ "linalg.sql_in", "linalg_8sql__in.html", null ],
      [ "linear.sql_in", "linear_8sql__in.html", null ],
      [ "lmf.sql_in", "lmf_8sql__in.html", null ],
      [ "logistic.sql_in", "logistic_8sql__in.html", null ],
      [ "multilogistic.sql_in", "multilogistic_8sql__in.html", null ],
      [ "online_sv.sql_in", "online__sv_8sql__in.html", null ],
      [ "prob.sql_in", "prob_8sql__in.html", null ],
      [ "profile.sql_in", "profile_8sql__in.html", null ],
      [ "quantile.sql_in", "quantile_8sql__in.html", null ],
      [ "rf.sql_in", "rf_8sql__in.html", null ],
      [ "sample.sql_in", "sample_8sql__in.html", null ],
      [ "sketch.sql_in", "sketch_8sql__in.html", null ],
      [ "summary.sql_in", "summary_8sql__in.html", null ],
      [ "svdmf.sql_in", "svdmf_8sql__in.html", null ],
      [ "svec.sql_in", "svec_8sql__in.html", null ],
      [ "utilities.sql_in", "utilities_8sql__in.html", null ],
      [ "utils_regularization.sql_in", null, null ],
      [ "viterbi.sql_in", "viterbi_8sql__in.html", null ]
    ] ],
    [ "File Members", "globals.html", null ]
  ] ]
];

function createIndent(o,domNode,node,level)
{
  if (node.parentNode && node.parentNode.parentNode)
  {
    createIndent(o,domNode,node.parentNode,level+1);
  }
  var imgNode = document.createElement("img");
  if (level==0 && node.childrenData)
  {
    node.plus_img = imgNode;
    node.expandToggle = document.createElement("a");
    node.expandToggle.href = "javascript:void(0)";
    node.expandToggle.onclick = function() 
    {
      if (node.expanded) 
      {
        $(node.getChildrenUL()).slideUp("fast");
        if (node.isLast)
        {
          node.plus_img.src = node.relpath+"ftv2plastnode.png";
        }
        else
        {
          node.plus_img.src = node.relpath+"ftv2pnode.png";
        }
        node.expanded = false;
      } 
      else 
      {
        expandNode(o, node, false);
      }
    }
    node.expandToggle.appendChild(imgNode);
    domNode.appendChild(node.expandToggle);
  }
  else
  {
    domNode.appendChild(imgNode);
  }
  if (level==0)
  {
    if (node.isLast)
    {
      if (node.childrenData)
      {
        imgNode.src = node.relpath+"ftv2plastnode.png";
      }
      else
      {
        imgNode.src = node.relpath+"ftv2lastnode.png";
        domNode.appendChild(imgNode);
      }
    }
    else
    {
      if (node.childrenData)
      {
        imgNode.src = node.relpath+"ftv2pnode.png";
      }
      else
      {
        imgNode.src = node.relpath+"ftv2node.png";
        domNode.appendChild(imgNode);
      }
    }
  }
  else
  {
    if (node.isLast)
    {
      imgNode.src = node.relpath+"ftv2blank.png";
    }
    else
    {
      imgNode.src = node.relpath+"ftv2vertline.png";
    }
  }
  imgNode.border = "0";
}

function newNode(o, po, text, link, childrenData, lastNode)
{
  var node = new Object();
  node.children = Array();
  node.childrenData = childrenData;
  node.depth = po.depth + 1;
  node.relpath = po.relpath;
  node.isLast = lastNode;

  node.li = document.createElement("li");
  po.getChildrenUL().appendChild(node.li);
  node.parentNode = po;

  node.itemDiv = document.createElement("div");
  node.itemDiv.className = "item";

  node.labelSpan = document.createElement("span");
  node.labelSpan.className = "label";

  createIndent(o,node.itemDiv,node,0);
  node.itemDiv.appendChild(node.labelSpan);
  node.li.appendChild(node.itemDiv);

  var a = document.createElement("a");
  node.labelSpan.appendChild(a);
  node.label = document.createTextNode(text);
  a.appendChild(node.label);
  if (link) 
  {
    a.href = node.relpath+link;
  } 
  else 
  {
    if (childrenData != null) 
    {
      a.className = "nolink";
      a.href = "javascript:void(0)";
      a.onclick = node.expandToggle.onclick;
      node.expanded = false;
    }
  }

  node.childrenUL = null;
  node.getChildrenUL = function() 
  {
    if (!node.childrenUL) 
    {
      node.childrenUL = document.createElement("ul");
      node.childrenUL.className = "children_ul";
      node.childrenUL.style.display = "none";
      node.li.appendChild(node.childrenUL);
    }
    return node.childrenUL;
  };

  return node;
}

function showRoot()
{
  var headerHeight = $("#top").height();
  var footerHeight = $("#nav-path").height();
  var windowHeight = $(window).height() - headerHeight - footerHeight;
  navtree.scrollTo('#selected',0,{offset:-windowHeight/2});
}

function expandNode(o, node, imm)
{
  if (node.childrenData && !node.expanded) 
  {
    if (!node.childrenVisited) 
    {
      getNode(o, node);
    }
    if (imm)
    {
      $(node.getChildrenUL()).show();
    } 
    else 
    {
      $(node.getChildrenUL()).slideDown("fast",showRoot);
    }
    if (node.isLast)
    {
      node.plus_img.src = node.relpath+"ftv2mlastnode.png";
    }
    else
    {
      node.plus_img.src = node.relpath+"ftv2mnode.png";
    }
    node.expanded = true;
  }
}

function getNode(o, po)
{
  po.childrenVisited = true;
  var l = po.childrenData.length-1;
  for (var i in po.childrenData) 
  {
    var nodeData = po.childrenData[i];
    po.children[i] = newNode(o, po, nodeData[0], nodeData[1], nodeData[2],
        i==l);
  }
}

function findNavTreePage(url, data)
{
  var nodes = data;
  var result = null;
  for (var i in nodes) 
  {
    var d = nodes[i];
    if (d[1] == url) 
    {
      return new Array(i);
    }
    else if (d[2] != null) // array of children
    {
      result = findNavTreePage(url, d[2]);
      if (result != null) 
      {
        return (new Array(i).concat(result));
      }
    }
  }
  return null;
}

function initNavTree(toroot,relpath)
{
  var o = new Object();
  o.toroot = toroot;
  o.node = new Object();
  o.node.li = document.getElementById("nav-tree-contents");
  o.node.childrenData = NAVTREE;
  o.node.children = new Array();
  o.node.childrenUL = document.createElement("ul");
  o.node.getChildrenUL = function() { return o.node.childrenUL; };
  o.node.li.appendChild(o.node.childrenUL);
  o.node.depth = 0;
  o.node.relpath = relpath;

  getNode(o, o.node);

  o.breadcrumbs = findNavTreePage(toroot, NAVTREE);
  if (o.breadcrumbs == null)
  {
    o.breadcrumbs = findNavTreePage("index.html",NAVTREE);
  }
  if (o.breadcrumbs != null && o.breadcrumbs.length>0)
  {
    var p = o.node;
    for (var i in o.breadcrumbs) 
    {
      var j = o.breadcrumbs[i];
      p = p.children[j];
      expandNode(o,p,true);
    }
    p.itemDiv.className = p.itemDiv.className + " selected";
    p.itemDiv.id = "selected";
    $(window).load(showRoot);
  }
}

