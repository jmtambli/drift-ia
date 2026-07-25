/* Drift Interiors + Architecture — client app.
   Galleries render from /data/*.json so the admin CMS can manage them. */
(function(){
  "use strict";
  var esc=function(s){return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');};
  function get(url){return fetch(url,{cache:'no-cache'}).then(function(r){return r.ok?r.json():Promise.reject(r.status);});}

  /* ---- Work gallery layout (mirrors the build's tile logic) ---- */
  function tiles(imgs){
    var n=imgs.length,t=[];
    if(n===0)return t;
    if(n===1)return [['half',imgs[0]],['half',imgs[0]]];
    t=[['big',imgs[0]],['small',imgs[1]]];
    var rest=imgs.slice(2),i=0;
    while(i<rest.length){
      var rem=rest.length-i;
      if(rem===1){t.push(['full',rest[i]]);i+=1;}
      else if(rem===2||rem===4){t.push(['half',rest[i]]);t.push(['half',rest[i+1]]);i+=2;}
      else{t.push(['third',rest[i]]);t.push(['third',rest[i+1]]);t.push(['third',rest[i+2]]);i+=3;}
    }
    return t;
  }
  function renderWork(){
    var root=document.getElementById('work-root'); if(!root) return Promise.resolve();
    return get('data/projects.json').then(function(d){var list=d.projects||d;
      root.innerHTML=list.map(function(p){
        var name=esc(p.name), cat=esc(p.category||''), loc=esc(p.location||''), imgs=p.images||[];
        var inner;
        if(p.compact && imgs.length){
          var hidden=imgs.slice(1).map(function(u){return '<span class="lb-src" data-full="'+esc(u)+'"></span>';}).join('');
          inner='<div class="tile full" data-full="'+esc(imgs[0])+'"><img src="'+esc(imgs[0])+'" alt="'+name+'" loading="lazy"></div>'+hidden;
        } else {
          inner=tiles(imgs).map(function(t){return '<div class="tile '+t[0]+'" data-full="'+esc(t[1])+'"><img src="'+esc(t[1])+'" alt="'+name+'" loading="lazy"></div>';}).join('');
        }
        return '<div class="project '+(p.compact?'compact ':'')+'reveal in" data-cat="'+cat+'">'
          +'<div class="project-head"><h3>'+name+'</h3><span class="loc"><span class="cat-tag">'+cat+'</span> &nbsp;/&nbsp; '+loc+'</span></div>'
          +'<div class="grid-gallery">'+inner+'</div></div>';
      }).join('');
    }).catch(function(){});
  }

  function renderUpcoming(){
    var root=document.getElementById('up-root'); if(!root) return Promise.resolve();
    return get('data/upcoming.json').then(function(d){var list=d.upcoming||d;
      root.innerHTML=list.map(function(p){
        var imgs=p.images||[]; if(!imgs.length) return '';
        var hidden=imgs.slice(1).map(function(u){return '<span class="lb-src" data-full="'+esc(u)+'"></span>';}).join('');
        return '<div class="up-card reveal in">'
          +'<div class="ph" data-full="'+esc(imgs[0])+'"><span class="status">'+esc(p.status||'')+'</span>'
          +'<img src="'+esc(imgs[0])+'" alt="'+esc(p.name)+' rendering" loading="lazy">'+hidden+'</div>'
          +'<div class="meta"><h3>'+esc(p.name)+'</h3><div class="t">'+esc(p.type||'')+'</div></div></div>';
      }).join('');
    }).catch(function(){});
  }

  function renderPlans(){
    var grid=document.getElementById('plan-grid'); if(!grid) return Promise.resolve();
    return get('data/plans.json').then(function(d){var list=d.plans||d;
      grid.innerHTML=list.map(function(p){
        var badge=p.approved?'<span class="badge">Approved &middot; Everett</span>':'';
        var scls=p.approved?'pstatus approved':'pstatus';
        var sqft=(typeof p.sqft==='number')?p.sqft.toLocaleString():esc(p.sqft);
        return '<article class="plan-card" data-type="'+esc(p.type)+'" data-size="'+esc(p.sqft)+'" data-name="'+esc((p.name||'').toLowerCase())+'">'
          +'<div class="ph">'+badge+'<img src="'+esc(p.image)+'" alt="'+esc(p.name)+' rendering" loading="lazy"></div>'
          +'<div class="pmeta"><h3>'+esc(p.name)+'</h3><div class="ptype">'+esc(p.type)+'</div>'
          +'<div class="specs">'+sqft+' sq ft &middot; '+esc(p.beds)+' bd &middot; '+esc(p.baths)+' ba</div>'
          +'<div class="'+scls+'">'+esc(p.status)+'</div>'
          +'<a class="tlink" href="contact.html">Inquire on Pricing &nearr;</a></div></article>';
      }).join('');
      // rebuild style filter options from data
      var ts=document.getElementById('plan-type');
      if(ts){var types=list.map(function(p){return p.type;}).filter(function(v,i,a){return v&&a.indexOf(v)===i;}).sort();
        ts.innerHTML='<option value="">All Styles</option>'+types.map(function(t){return '<option>'+esc(t)+'</option>';}).join('');}
    }).catch(function(){});
  }

  /* ---- interactions (bound after render) ---- */
  function initReveal(){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12});
    document.querySelectorAll('.reveal:not(.in)').forEach(function(el){io.observe(el);});
  }
  function initLightbox(){
    var lb=document.getElementById('lb'); if(!lb) return;
    var img=lb.querySelector('img'),list=[],i=0;
    function show(){img.src=list[i];}
    document.querySelectorAll('[data-full]').forEach(function(el){
      el.onclick=function(){
        list=[].slice.call(document.querySelectorAll('.project:not(.hide) [data-full], #up-root [data-full], #plan-grid [data-full]')).map(function(x){return x.dataset.full;});
        if(!list.length){list=[el.dataset.full];}
        i=Math.max(0,list.indexOf(el.dataset.full)); show(); lb.classList.add('open');
      };
    });
    lb.querySelector('.close').onclick=function(){lb.classList.remove('open');};
    lb.querySelector('.next').onclick=function(e){e.stopPropagation();i=(i+1)%list.length;show();};
    lb.querySelector('.prev').onclick=function(e){e.stopPropagation();i=(i-1+list.length)%list.length;show();};
    lb.addEventListener('click',function(e){if(e.target===lb)lb.classList.remove('open');});
    document.addEventListener('keydown',function(e){if(!lb.classList.contains('open'))return;if(e.key==='Escape')lb.classList.remove('open');if(e.key==='ArrowRight')lb.querySelector('.next').click();if(e.key==='ArrowLeft')lb.querySelector('.prev').click();});
  }
  function initWorkFilters(){
    var btns=document.querySelectorAll('.filters button'); if(!btns.length) return;
    btns.forEach(function(b){b.onclick=function(){
      btns.forEach(function(x){x.classList.remove('active');});b.classList.add('active');
      var f=b.dataset.filter;
      document.querySelectorAll('.project').forEach(function(p){p.classList.toggle('hide', f!=='all' && p.dataset.cat!==f);});
    };});
  }
  function initPlansFilter(){
    var grid=document.getElementById('plan-grid'); if(!grid) return;
    var q=document.getElementById('plan-q'),ts=document.getElementById('plan-type'),ss=document.getElementById('plan-size');
    var count=document.getElementById('plan-count'),empty=document.getElementById('plan-empty');
    function apply(){
      var cards=[].slice.call(grid.querySelectorAll('.plan-card'));
      var qq=(q.value||'').trim().toLowerCase(),tv=ts.value,sv=ss.value,lo=0,hi=1e9;
      if(sv){var pr=sv.split('-');lo=+pr[0];hi=+pr[1];}
      var n=0;
      cards.forEach(function(c){var sz=+c.dataset.size;
        var ok=(!qq||c.dataset.name.indexOf(qq)>-1)&&(!tv||c.dataset.type===tv)&&(sz>=lo&&sz<=hi);
        c.classList.toggle('hide',!ok); if(ok)n++;});
      if(count)count.textContent=n+(n===1?' plan':' plans')+' shown';
      if(empty)empty.hidden=n!==0;
    }
    [q,ts,ss].forEach(function(el){el.addEventListener('input',apply);}); apply();
  }
  function initForm(){
    var form=document.querySelector('.lead-form'); if(!form) return;
    var success=document.querySelector('.form-success');
    form.addEventListener('submit',function(e){
      e.preventDefault(); if(!form.reportValidity())return;
      var btn=form.querySelector('button[type=submit]'); if(btn){btn.disabled=true;btn.textContent='Sending…';}
      var data=new URLSearchParams(new FormData(form)).toString();
      fetch(form.getAttribute('action')||'/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:data}).catch(function(){}).then(function(){
        form.style.display='none'; if(success){success.hidden=false;success.scrollIntoView({behavior:'smooth',block:'center'});}
      });
    });
  }

  function applyContent(){
    return get('data/content.json').then(function(c){
      Object.keys(c).forEach(function(k){
        var v=c[k]; if(v==null||v==='' || typeof v==='object') return;
        document.querySelectorAll('[data-cms="'+k+'"]').forEach(function(el){
          if(k==='email'){ el.textContent=v; if(el.tagName==='A') el.href='mailto:'+v; }
          else if(k==='phone'){ el.textContent=v; if(el.tagName==='A') el.href='tel:'+v.replace(/[^0-9+]/g,''); }
          else { el.innerHTML=v; }
        });
      });
      // social links: set href + reveal; hide when empty
      var anySocial=false;
      if(c.social){ Object.keys(c.social).forEach(function(k){
        var url=c.social[k];
        document.querySelectorAll('[data-social="'+k+'"]').forEach(function(el){
          if(url){ el.href=url; el.hidden=false; anySocial=true; } else { el.hidden=true; }
        });
      }); }
      var se=document.getElementById('soc-empty'); if(se) se.hidden=anySocial;
      // instagram feed embed (paste widget code in admin)
      if(c.instagramEmbed){ var box=document.getElementById('ig-embed'); if(box) box.innerHTML=c.instagramEmbed; }
    }).catch(function(){});
  }
  /* ---- Journal (blog) ---- */
  function md(t){
    t=String(t||'');
    // escape then re-allow our markdown
    t=t.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
    var blocks=t.split(/\n{2,}/).map(function(b){
      b=b.trim();
      if(/^### /.test(b)) return '<h3>'+inline(b.replace(/^### /,''))+'</h3>';
      if(/^## /.test(b))  return '<h2>'+inline(b.replace(/^## /,''))+'</h2>';
      if(/^# /.test(b))   return '<h2>'+inline(b.replace(/^# /,''))+'</h2>';
      if(/^(-|\*) /.test(b)){
        var items=b.split(/\n/).map(function(li){return '<li>'+inline(li.replace(/^(-|\*) /,''))+'</li>';}).join('');
        return '<ul>'+items+'</ul>';
      }
      return '<p>'+inline(b.replace(/\n/g,'<br>'))+'</p>';
    });
    return blocks.join('');
    function inline(x){
      return x.replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>')
              .replace(/\*([^*]+)\*/g,'<em>$1</em>')
              .replace(/\[([^\]]+)\]\(([^)]+)\)/g,'<a href="$2" target="_blank" rel="noopener">$1</a>');
    }
  }
  var POSTS=[];
  function fmtDate(s){ try{var d=new Date(s+'T00:00:00');return d.toLocaleDateString('en-US',{year:'numeric',month:'long',day:'numeric'});}catch(e){return s;} }
  function renderJournal(){
    var root=document.getElementById('journal-root'); if(!root) return Promise.resolve();
    return get('data/journal.json').then(function(d){ POSTS=d.posts||d;
      root.innerHTML=POSTS.map(function(p,idx){
        return '<article class="post-card reveal in" data-idx="'+idx+'">'
          +'<div class="ph"><img src="'+esc(p.cover)+'" alt="'+esc(p.title)+'" loading="lazy"></div>'
          +'<div class="pmeta"><div class="pdate">'+esc(fmtDate(p.date))+'</div>'
          +'<h3>'+esc(p.title)+'</h3><p class="pex">'+esc(p.excerpt||'')+'</p>'
          +'<span class="tlink">Read the story &nearr;</span></div></article>';
      }).join('');
      root.querySelectorAll('.post-card').forEach(function(c){c.onclick=function(){openPost(+c.dataset.idx);};});
    }).catch(function(){});
  }
  function openPost(i){
    var r=document.getElementById('reader'); if(!r||!POSTS[i])return;
    var p=POSTS[i];
    r.querySelector('.reader-inner').innerHTML=
      '<div class="reader-cover"><img src="'+esc(p.cover)+'" alt="'+esc(p.title)+'"></div>'
      +'<div class="reader-body"><div class="pdate">'+esc(fmtDate(p.date))+'</div><h1>'+esc(p.title)+'</h1>'+md(p.body)+'</div>';
    r.classList.add('open'); document.body.style.overflow='hidden';
    r.scrollTop=0;
  }
  function initReader(){
    var r=document.getElementById('reader'); if(!r)return;
    function close(){r.classList.remove('open');document.body.style.overflow='';}
    r.querySelector('.reader-close').onclick=close;
    document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});
  }

  document.addEventListener('DOMContentLoaded',function(){
    applyContent();
    Promise.all([renderWork(),renderUpcoming(),renderPlans(),renderJournal()]).then(function(){
      initReveal(); initLightbox(); initWorkFilters(); initPlansFilter(); initForm(); initReader();
    });
  });
})();
