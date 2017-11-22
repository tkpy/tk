  /*公共导航部分--------------------------------------*/
  //顶部导航鼠标经过出现内容
  function topNav(){
    for(var i =1;i<5;i++){
      $('.layout-header-nav li').eq(i).mouseover(function(){
        var $this = $('.layout-header-nav-child');
        var lw = $('.layout-header-nav-child-list li').width();
        var t = $('.layout-header-nav-child-list li').length;
        var uw = lw * t /2;
        $this.show();
        $this.find('.layout-header-nav-child-list').css('margin-left',-uw);
        }).mouseout(function(){
          $('.layout-header-nav-child').hide();
        });
    }
 }//顶部导航鼠标经过出现内容 E

  function topLogin(){
      // 登录图片鼠标经过
      $('#layoutHeaderUser').mouseover(function(){
        $('.layout-user-downmenu').show();
      }).mouseout(function() {
          $('.layout-user-downmenu').hide();
      });
  }
  // 公共返回顶部
  function backTop(){
    $(window).scroll(function(){
      var dTop = $(document).scrollTop();
      var fTop = $('.layout-header .navbar').height();
      if(dTop >fTop){
        $('.layout-magnet').show();
      }else{
        $('.layout-magnet').hide();
      }
    });
    $(".layout-magnet").click(function(){
      $("html").animate({"scrollTop": "0px"},500); //IE,FF
      $("body").animate({"scrollTop": "0px"},500); //Webkit
    });
  } 
  /*---------------------------------------------------*/ 

  /*首页部分-------------------------------------------*/
  // 首页侧导航鼠标经过出现内容
  function leftNav(){
    $('#homeCategory li').mouseover(function(){
      $(this).find('.home-category-child').show();
    }).mouseout(function(){
      $(this).find('.home-category-child').hide();
    })
  }

  /*---------------------------------------------------*/ 

  /*全部商品部分---------------------------------------*/
  function comPro(){
    $(".gl-item").mouseover(function(){
      $(this).find('.compare-btn-list').css('display','block');
    });
    $(".gl-item").mouseout(function(){
      $(this).find('.compare-btn-list').css('display','none');
    });

  }

  /*---------------------------------------------------*/ 

  /*产品详情页部分-------------------------------------*/
  function  detaNav(){
    $('#detailFast ul li').click(function(){
      var t = $(this).index();
      
      $('#detailFast ul li').addClass('current').siblings().removeClass('current');
      $('.detail-content div').eq(t).addClass('current').siblings().removeClass('current');
    })
      $(window).scroll(function(){
        var dt = $('#detail').offset().top;
        var dTop = $(document).scrollTop();
        if(dTop >= dt){
          $('#detailFast').addClass('float-nav');
        }else{
          $('#detailFast').removeClass('float-nav');
        }
        //console.log(dt,dTop)
      })
    } 
     // 数量增加减少
    function addMin(){
      // 减少
      $('.vm-minus').click(function(){
          var n=$('#J_quantity').val(); //减号
          var num=parseInt(n)-1;
          if(num<=1){ 
            $('.vm-minus').addClass('disabled');
            $(this).next().val(1);
          }else{
            $('.vm-minus').removeClass('disabled');
            $(this).next().val(num);
          }
          
      })
      //增加 加号
      $('.vm-plus').click(function(){
          var n=$('#J_quantity').val();
          var num=parseInt(n)+1;
          if(num>1){ $('.vm-minus').removeClass('disabled');}
          $(this).prev().val(num);
          })
      //丧失焦点事件
      $('#J_quantity').blur(function(){
        var n = $(this).val();
        if(n==""){
          $(this).val(1)
        }
        else{
          if (isNaN(n)){
            $(this).val(1)
          }
          else{
            n = parseInt(n)
            if(n<1){
              $(this).val(1)
            }
            else{
              $(this).val(n)
            }
          }
        }
      })
      }// 数量增加减少E

  /*---------------------------------------------------*/ 
  /*移动端特效-----------------------------------------*/
  function appTopNav(){
    $(window).scroll(function(){
      var dTop = $(document).scrollTop();
      if(dTop>0){
        $('#J_listFilter').addClass('fixed');
      }else{
        $('#J_listFilter').removeClass('fixed');
      }
    })
  }
  /*---------------------------------------------------*/ 
  

/*购物车--------------------------------------------*/ 

//选择框操作
function allSelect(){
  var aee = false;
  var see = false;
  // 全选
  $('.JSelectAll .mz-checkbox').click(function(){
    if(aee==false){
      $(this).addClass('checked');
      $('.cart-col-select .mz-checkbox').addClass('checked');
      //全部选中后获取小计的
      //计算金额
      loadTotal()
      aee = true;
    }else if(aee==true){
      $(this).removeClass('checked');
      $('.cart-col-select .mz-checkbox').removeClass('checked');
      //计算金额
      loadTotal()
      aee = false;
    }
  })

  //单选
  $('.cart-col-select .mz-checkbox').click(function(){
    if(see==false){
      $(this).addClass('checked');
      //计算金额
      loadTotal()
      see = true;
    }else if(see==true){
      $(this).removeClass('checked');
      //计算金额
      loadTotal()
      see = false;
    }
  })

}
//计算商品数量和总金额
function loadTotal(){
  var ids=[]  //获取已经选择的单个商品
  
  // alert('金额统计计算')
  var list = $("table.cart-merchant-body div.mz-checkbox").filter(".checked")
  $("#totalCount").html(list.length)
  var total = 0.0
  for (var i = 0; i < list.length; i++) {
    total += parseFloat($(list[i]).attr('price'))
    ids.push($(list[i]).attr('gid'))
  };
  $("#totalPrice").html(total)
  return ids
}
// 数量增加减少
function cartAddMin(){
      // 减少
      $('.mz-adder-subtract').click(function(){
          //检测操作的是哪个商品
           var fzhi=$(this).parents('.cart-product').attr('id');
           var reg=/^pro\d$/;
           var prod=reg.exec(fzhi);

           //商品展示个数、减号、超过数量的文本
           var $mText = $(this).parents('#'+prod).find('.cart-product-number-max');
           var $nSub = $(this).parents('#'+prod).find('.mz-adder-subtract');//查找减号
           var n=$(this).next().children().val()
           var num=parseInt(n)

           

           //获取当前商品的单价和小计
           var $nPrice = $(this).parents('#'+prod).find('.cart-col-price .cart-product-price');//当前商品的单价
           var npText = parseInt($nPrice.text());//单价的值
           var $sumPrice = $(this).parents('#'+prod).find('.cart-col-total  .cart-product-price');//当前商品的小计
           var spText = parseInt($sumPrice.text());//小计的值

           
           

          //商品减少操作
          if(num<=1){
            // alert('呵呵哒') 
            $('.mz-adder-subtract').addClass('disabled');
            $(this).next().children().val(1)
            $sumPrice.html(npText+'.00')//显示单价的值
          }else{
            // alert('哈哈')
            $('.mz-adder-subtract').removeClass('disabled');
            num = num-1
            $(this).next().children().val(num)
            //单个商品的小计
            spText= spText - npText;//小计的值
            $sumPrice.html(spText+'.00');//显示小计的值
          }

          //计算金额
          loadTotal()
          
      })
      //增加 加号
      $('.mz-adder-add').click(function(){
          //检测操作的是哪个商品
           var fzhi=$(this).parents('.cart-product').attr('id');
           var reg=/^pro\d$/;
           var prod=reg.exec(fzhi);

           //商品展示个数、加号、超过数量的文本
           var $nAdd = $(this).parents('#'+prod).find('.mz-adder-add');
           var $nSub = $(this).parents('#'+prod).find('.mz-adder-subtract');
           var $nInput = $(this).parents('#'+prod).find('.mz-adder-input');
           var n=$nInput.val();
           var $mText = $(this).parents('#'+prod).find('.cart-product-number-max');
           var num=parseInt(n)+1;

           //获取当前商品的单价和小计
           var $nPrice = $(this).parents('#'+prod).find('.cart-col-price .cart-product-price');
           var npText = parseInt($nPrice.text());
           var $sumPrice = $(this).parents('#'+prod).find('.cart-col-total  .cart-product-price');
           var spText = parseInt($sumPrice.text());

          //商品增加操作
          var n=$(this).prev().children().val();
          var num=parseInt(n)+1;
          if(num>1){ $('.mz-adder-subtract').removeClass('disabled');}
          $(this).prev().children().val(num);
          
        //单个商品的小计
           spText= spText + npText;
           $sumPrice.html(spText+'.00');
           // console.log(num);

          //计算金额
          loadTotal()

           })

      //丧失焦点事件
      $('.mz-adder-input').blur(function(){

        //检测操作的是哪个商品
         var fzhi=$(this).parents('.cart-product').attr('id');
         var reg=/^pro\d$/;
         var prod=reg.exec(fzhi);
         
         //获取当前商品的单价和小计
         var $nPrice = $(this).parents('#'+prod).find('.cart-col-price .cart-product-price');//当前商品的单价
         var npText = parseInt($nPrice.text());//单价的值
         var $sumPrice = $(this).parents('#'+prod).find('.cart-col-total  .cart-product-price');//当前商品的小计
         var spText = parseInt($sumPrice.text());//小计的值

         var n = $(this).val();

        if(n==""){
          $(this).val(1)
          $sumPrice.html(npText+'.00')//显示为单价的值
        }
        else{
          if (isNaN(n)){
            $(this).val(1)
            $sumPrice.html(npText+'.00')//显示为单价的值
          }
          else{
            n = parseInt(n)
            if(n<1){
              $(this).val(1)
              $sumPrice.html(npText+'.00')//显示为单价的值
            }
            else{
              $(this).val(n)
              $sumPrice.html(npText*n+'.00')//显示为单价的值
            }
          }
        }
        //计算金额
        loadTotal()

      })

      //叉号删除商品
      $('.cart-product-remove').click(function(){
            $(this).parents('.cart-product').remove();
      })

    
}// 数量增加减少E 




/*---------------------------------------------------*/ 



/*登录页面----------------------------------------*/ 
function nLogin(){
      //   提交
      var UserOk=false;
      var passOk=false;
      //绑定表单的提交事件
       $('.main-form').submit(function(){
         //触发所有的丧失焦点事件
         // $('input').trigger('blur');
         //判断字段是否正确
         if(UserOk && passOk){
           //都正确就可以提交
           return true;
         }else{
           //有一个错误都不能提交
           
           // alert(UserOk,passOk)
           if(UserOk==false){
              $('.tip-box').removeClass('visiblility-hidden');
              $('.tip-box .tip-font').html("用户名不符合要求");
           }
           if(passOk==false){
                $('.tip-box').removeClass('visiblility-hidden');
              $('.tip-box .tip-font').html("密码不符合要求");
           }
           return false;
         }
       })
      //丧失焦点事件
     $('input[name=username]').blur(function(){
          //获取用户输入的信息.进行验证
              var v = $(this).val();
              //进行正则验证
              var reg = /^.{3,18}$/;
              if(reg.test(v)){
                // alert('用户名符合要求')
                UserOk = true;
              }else{
                // alert('用户名不符合要求')
                $('.tip-box').removeClass('visiblility-hidden');
                $('.tip-box .tip-font').html("请输入至少3位数的用户名");
                UserOk = false;
              }
     })

      //丧失焦点事件
     $('input[name=password]').blur(function(){
          //获取用户信息
          var v =$(this).val();
          var reg=/^\w{6,18}$/;
          //判断如果为true则通过
          if(reg.test(v)){
                // $('.passwd-box').removeClass('btn-error');
                $('.tip-box').addClass('visiblility-hidden');
                passOk=true;
          }else{
                // $('.passwd-box').addClass('btn-error');
                $('.tip-box').removeClass('visiblility-hidden');
                $('.tip-box .tip-font').html("请输入正确的密码")
                passOk=false;
          }
     })
     //获取焦点事件
     $('input[name=username]').focus(function(){
        $('.tip-box').removeClass('visiblility-hidden');
        $('.tip-box .tip-font').html("用户名至少3位数")
      })
     $('input[name=password]').focus(function(){
        $('.tip-box').removeClass('visiblility-hidden');
        $('.tip-box .tip-font').html("密码至少6位数");
     })

     $('input[name!=submit]').blur(function(){
      $('.tip-box').addClass('visiblility-hidden');
     })

}



/*---------------------------------------------------*/ 