
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 00:42:24 2022
@author: Jordi Garcia Ruspira
"""


import streamlit as st
import pandas as pd
import requests
import json
import time
import plotly.graph_objects as go
import random
import plotly.io as pio 

st.set_page_config(
		page_title="Cosmos Validators - Proposal 82 - Sankey chart",
		page_icon=":atom_symbol:",
		layout="wide",
		menu_items=dict(About="It's a work of Jordi"),
)


st.title(":atom_symbol: Cosmos Sankey :atom_symbol:")


st.success("This app only two charts! Please select a validator ")
st.text("")
st.subheader('Streamlit App by [Jordi R.](https://twitter.com/RuspiTorpi/). Powered by Flipsidecrypto')
st.text("")
st.markdown('Hi there. For more insights please refer to my Flipsidecrypto dashboard on the subject. This streamlit app displays a Sankey chart redelegations from a selected validator to the rest of validators between the time proposal 82 went live and current date.' )   


st.markdown(
			f"""
	<style>
		.reportview-container .main .block-container{{
			max-width: 90%;
			padding-top: 5rem;
			padding-right: 5rem;
			padding-left: 5rem;
			padding-bottom: 5rem;
		}}
		img{{
			max-width:40%;
			margin-bottom:40px;
		}}
	</style>
	""",
			unsafe_allow_html=True,
		) 
pio.renderers.default = 'browser'




API_KEY = st.secrets["API_KEY"]

 

SQL_QUERY_2 = """ with table_8 as (
select distinct tx_id from cosmos.core.fact_msg_attributes
where tx_succeeded = 'TRUE'
and msg_type = 'message'
and attribute_key = 'action'
and attribute_value = '/cosmos.staking.v1beta1.MsgBeginRedelegate'
and to_date(block_timestamp) between '2022-10-31' and current_date 
),

table_9 as (select distinct tx_id, attribute_value as address from cosmos.core.fact_msg_attributes
where tx_succeeded = 'TRUE'
and msg_type = 'transfer'
and attribute_key = 'sender'
and msg_index = '2'
and tx_id in (select * from table_8)),

table_10 as (select distinct tx_id, attribute_value as validator_from from cosmos.core.fact_msg_attributes
where tx_succeeded = 'TRUE'
and msg_type = 'redelegate'
and attribute_key = 'source_validator'
and tx_id in (select * from table_8)),

  
table_11 as (select distinct tx_id, attribute_value as validator_to from cosmos.core.fact_msg_attributes
where tx_succeeded = 'TRUE'
and msg_type = 'redelegate'
and attribute_key = 'destination_validator'
and tx_id in (select * from table_8)),

  table_12 as (select distinct tx_id, to_number(SUBSTRING(attribute_value,0,CHARINDEX('uatom',attribute_value)-1))/pow(10,6) as amount from cosmos.core.fact_msg_attributes
where tx_succeeded = 'TRUE'
and msg_type = 'redelegate'
and attribute_key = 'amount'
and tx_id in (select * from table_8))



  
select 
case when b.validator_from = 'cosmosvaloper1sjllsnramtg3ewxqwwrwjxfgc4n4ef9u2lcnj0' then 'Stake fish '

  when b.validator_from = 'cosmosvaloper1c4k24jzduc365kywrsvf5ujz4ya6mwympnc4en' then 'Coinbase Custody'
 when b.validator_from = 'cosmosvaloper14lultfckehtszvzw4ehu0apvsr77afvyju5zzy' then 'DokiaCapital'
 when b.validator_from = 'cosmosvaloper1v5y0tg0jllvxf5c3afml8s3awue0ymju89frut' then 'Zero Knowledge Validator (ZKV)'
 when b.validator_from = 'cosmosvaloper196ax4vc0lwpxndu9dyhvca7jhxp70rmcvrj90c' then 'SG-1'
 when b.validator_from = 'cosmosvaloper18ruzecmqj9pv8ac0gvkgryuc7u004te9rh7w5s' then 'Binance node'
 when b.validator_from = 'cosmosvaloper14k4pzckkre6uxxyd2lnhnpp8sngys9m6hl6ml7' then 'Polychain'
 when b.validator_from = 'cosmosvaloper1tflk30mq5vgqjdly92kkhhq3raev2hnz6eete3' then 'Everstake'
 when b.validator_from = 'cosmosvaloper1qaa9zej9a0ge3ugpx3pxyx602lxh3ztqgfnp42' then 'Game'
 when b.validator_from = 'cosmosvaloper19lss6zgdh5vvcpjhfftdghrpsw7a4434elpwpu' then 'Paradigm'
 when b.validator_from = 'cosmosvaloper1ey69r37gfxvxg62sh4r0ktpuc46pzjrm873ae8' then 'Sika'
 when b.validator_from = 'cosmosvaloper1hjct6q7npsspsg3dgvzk3sdf89spmlpfdn6m9d' then 'Figment'
 when b.validator_from = 'cosmosvaloper1clpqr4nrk4khgkxj78fcwwh6dl3uw4epsluffn' then 'Cosmostation'
 when b.validator_from = 'cosmosvaloper156gqf9837u7d4c4678yt3rl4ls9c5vuursrrzf' then 'Binance staking'
 when b.validator_from = 'cosmosvaloper132juzk0gdmwuxvx4phug7m3ymyatxlh9734g4w' then 'P2P.org'
 when b.validator_from = 'cosmosvaloper15urq2dtp9qce4fyc85m6upwm9xul3049e02707' then 'Chorus One'
 when b.validator_from = 'cosmosvaloper1z8zjv3lntpwxua0rtpvgrcwl0nm0tltgpgs6l7' then 'Kraken'
 when b.validator_from = 'cosmosvaloper1vf44d85es37hwl9f4h9gv0e064m0lla60j9luj' then 'Multichain ventures'
 when b.validator_from = 'cosmosvaloper16k579jk6yt2cwmqx9dz5xvq9fug2tekvlu9qdv' then 'Informal systems'
 when b.validator_from = 'cosmosvaloper1zqgheeawp7cmqk27dgyctd80rd8ryhqs6la9wc' then 'No fee to 2025'
 when b.validator_from = 'cosmosvaloper1g48268mu5vfp4wk7dk89r0wdrakm9p5xk0q50k' then 'Provalidator'
 when b.validator_from = 'cosmosvaloper1lzhlnpahvznwfv4jmay2tgaha5kmz5qxerarrl' then 'Citadel.one'
 when b.validator_from = 'cosmosvaloper1gpx52r9h3zeul45amvcy2pysgvcwddxrgx6cnv' then 'StakeLab'
 when b.validator_from = 'cosmosvaloper1qwl879nx9t6kef4supyazayf7vjhennyh568ys' then 'Certus One'
 when b.validator_from = 'cosmosvaloper1gdg6qqe5a3u483unqlqsnullja23g0xvqkxtk0' then 'Zugerselfdelegation'
 when b.validator_from = 'cosmosvaloper1n229vhepft6wnkt5tjpwmxdmcnfz55jv3vp77d' then 'Allnodes.com'
 when b.validator_from = 'cosmosvaloper1ma02nlc7lchu7caufyrrqt4r6v2mpsj90y9wzd' then 'Hashtower'
 when b.validator_from = 'cosmosvaloper1vvwtk805lxehwle9l4yudmq6mn0g32px9xtkhc' then 'Imperator.co'
 when b.validator_from = 'cosmosvaloper1eh5mwu044gd5ntkkc2xgfg8247mgc56fz4sdg3' then 'Boubounode'
 when b.validator_from = 'cosmosvaloper1grgelyng2v6v3t8z87wu3sxgt9m5s03xfytvz7' then 'Inqlusion'
 when b.validator_from = 'cosmosvaloper1te8nxpc2myjfrhaty0dnzdhs5ahdh5agzuym9v' then 'CoinoneNode'
 when b.validator_from = 'cosmosvaloper1rpgtz9pskr5geavkjz02caqmeep7cwwpv73axj' then 'Blockpower'
 when b.validator_from = 'cosmosvaloper14kn0kk33szpwus9nh8n87fjel8djx0y070ymmj' then 'Forbole'
 when b.validator_from = 'cosmosvaloper1y0us8xvsvfvqkk9c6nt5cfyu5au5tww2ztve7q' then 'Swiss Staking'
 when b.validator_from = 'cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p' then 'Staking Facilities'
 when b.validator_from = 'cosmosvaloper130mdu9a0etmeuw52qfxk73pn0ga6gawkxsrlwf' then 'strangelove-ventures'
 when b.validator_from = 'cosmosvaloper16fnz0v4cnv5dpnj0p3gaft2q2kzx8z5hfrx6v5' then 'DACM'
 when b.validator_from = 'cosmosvaloper1we6knm8qartmmh2r0qfpsz6pq0s7emv3e0meuw' then 'Staked'
 when b.validator_from = 'cosmosvaloper1jst8q8flpn94u9uvkpae8mrkk3a5pjhxx529z2' then 'Node Guardians'
 when b.validator_from = 'cosmosvaloper10e4vsut6suau8tk9m6dnrm0slgd6npe3jx5xpv' then 'B-Harvest'
 when b.validator_from = 'cosmosvaloper1kgddca7qj96z0qcxr2c45z73cfl0c75p7f3s2e' then 'ChainLayer'
 when b.validator_from = 'cosmosvaloper1cc99d3xcukhedg4wcw53j7a9q68uza707vpfe7' then 'dForce'
 when b.validator_from = 'cosmosvaloper19rmlxkqjt950fxl849l49x0me56u9tkd5n5j62' then 'Post Road'
 when b.validator_from = 'cosmosvaloper199mlc7fr6ll5t54w7tts7f4s0cvnqgc59nmuxf' then 'ShapeShift DAO'
 when b.validator_from = 'cosmosvaloper1k2d9ed9vgfuk2m58a2d80q9u6qljkh4vfaqjfq' then 'Stakecito'
 when b.validator_from = 'cosmosvaloper10wljxpl03053h9690apmyeakly3ylhejrucvtm' then 'Ledger'
 when b.validator_from = 'cosmosvaloper1uutuwrwt3z2a5z8z3uasml3rftlpmu25aga5c6' then 'DelegaNetworks '
 when b.validator_from = 'cosmosvaloper1ssm0d433seakyak8kcf93yefhknjleeds4y3em' then 'IRISnet-Bianjie'
 when b.validator_from = 'cosmosvaloper1ehkfl7palwrh6w2hhr2yfrgrq8jetgucudztfe' then 'KalpaTech'
 when b.validator_from = 'cosmosvaloper19yy989ka5usws6gsd8vl94y7l6ssgdwsrnscjc' then 'OKEx Pool'
 when b.validator_from = 'cosmosvaloper1hjadhj9nqzpye2vkmkz4thahhd0z8dh3udhq74' then 'Atomic Nodes'
 when b.validator_from = 'cosmosvaloper157v7tczs40axfgejp2m43kwuzqe0wsy0rv8puv' then 'POSTHUMAN DVS'
 when b.validator_from = 'cosmosvaloper1gxju9ky3hwxvqqagrl3dxtl49kjpxq6wlqe6m5' then 'Vortex.live'
 when b.validator_from = 'cosmosvaloper1n3mhyp9fvcmuu8l0q8qvjy07x0rql8q46fe2xk' then '0base.vc'
 when b.validator_from = 'cosmosvaloper146kwpzhmleafmhtaxulfptyhnvwxzlvm87hwnm' then 'KysenPool Sky'
 when b.validator_from = 'cosmosvaloper1x8efhljzvs52u5xa6m7crcwes7v9u0nlwdgw30' then 'Upbit Staking'
 when b.validator_from = 'cosmosvaloper14l0fp639yudfl46zauvv8rkzjgd4u0zk2aseys' then 'ATEAM'
 when b.validator_from = 'cosmosvaloper13nvnv6q8d3yg7tjeahjzljkqu0y27s8y9e7as9' then 'Latent Iron'
 when b.validator_from = 'cosmosvaloper1dqp325was50l7ut2lnx6s8xhmtwj3wrtx06gzu' then 'Nocturnal Labs'
 when b.validator_from = 'cosmosvaloper1lktjhnzkpkz3ehrg8psvmwhafg56kfss3q3t8m' then 'Umbrella '
 when b.validator_from = 'cosmosvaloper1udpsgkgyutgsglauk9vk9rs03a3skc62gup9ny' then 'AUDIT.one'
 when b.validator_from = 'cosmosvaloper10nzaaeh2kq28t3nqsh5m8kmyv90vx7ym5mpakx' then 'Blockdaemon'
 when b.validator_from = 'cosmosvaloper1sd4tl9aljmmezzudugs7zlaya7pg2895ws8tfs' then 'InfStones'
 when b.validator_from = 'cosmosvaloper124maqmcqv8tquy764ktz7cu0gxnzfw54n3vww8' then 'Simply Staking'
 when b.validator_from = 'cosmosvaloper1uhnsxv6m83jj3328mhrql7yax3nge5svrv6t6c' then 'S16 Research Ventures'
 when b.validator_from = 'cosmosvaloper1ptyzewnns2kn37ewtmv6ppsvhdnmeapvtfc9y5' then 'WeStaking'
 when b.validator_from = 'cosmosvaloper157qezau9xnzypse3vu2vhs7r4ee83fdecew0fz' then 'KuCoin'
 when b.validator_from = 'cosmosvaloper1ul2me6vukg2vac2p6ltxmqlaa7jywdgt8q76ag' then 'HyperblocksPro'
 when b.validator_from = 'cosmosvaloper17mggn4znyeyg25wd7498qxl7r2jhgue8u4qjcq' then '01node'
 when b.validator_from = 'cosmosvaloper1q6d3d089hg59x6gcx92uumx70s5y5wadklue8s' then 'Ubik Capital 0%Fee'
 when b.validator_from = 'cosmosvaloper1sxx9mszve0gaedz5ld7qdkjkfv8z992ax69k08' then 'e-Money.com // validator.network'
 when b.validator_from = 'cosmosvaloper1lcwxu50rvvgf9v6jy6q5mrzyhlszwtjxhtscmp' then 'stakezone'
 when b.validator_from = 'cosmosvaloper1dt93l3qgmhhlp97srjyqyendrgu9nx0suxtwe8' then '天照☀'
 when b.validator_from = 'cosmosvaloper1ej2es5fjztqjcd4pwa0zyvaevtjd2y5wxxp9gd' then 'Frens '
 when b.validator_from = 'cosmosvaloper1gjtvly9lel6zskvwtvlg5vhwpu9c9waw7sxzwx' then 'EZStaking.io'
 when b.validator_from = 'cosmosvaloper1r2dthxctqzhwg299e7aaeqwfkgcc9hg8k3yd7m' then '0% Fee 🌻 Sunflower'
 when b.validator_from = 'cosmosvaloper1pjmngrwcsatsuyy8m3qrunaun67sr9x7z5r2qs' then 'Cypher Core'
 when b.validator_from = 'cosmosvaloper10jzj3jjd3frna0ay08sh4zu4fpy957s49jkk7m' then 'Onbloc Node'
 when b.validator_from = 'cosmosvaloper1m73mgwn3cm2e8x9a9axa0kw8nqz8a492ms63vn' then '#decentralizehk - DHK dao'
 when b.validator_from = 'cosmosvaloper1symf474wnypes2d3mecllqk6l26rwz8mfjqdus' then 'BlockHunters '
 when b.validator_from = 'cosmosvaloper1hdrlqvyjfy5sdrseecjrutyws9khtxxaux62l7' then 'SmartNodes'
 when b.validator_from = 'cosmosvaloper17h2x3j7u44qkrq0sk8ul0r2qr440rwgjkfg0gh' then 'FreshATOMS.com'
 when b.validator_from = 'cosmosvaloper1gf4wlkutql95j7wwsxz490s6fahlvk2s9xpwax' then 'Stakewolle.com | Auto-compound'
 when b.validator_from = 'cosmosvaloper1cgh5ksjwy2sd407lyre4l3uj2fdrqhpkzp06e6' then 'HashQuark'
 when b.validator_from = 'cosmosvaloper13sduv92y3xdhy3rpmhakrc3v7t37e7ps9l0kpv' then 'nylira.net'
 when b.validator_from = 'cosmosvaloper1gp957czryfgyvxwn3tfnyy2f0t9g2p4pqeemx8' then 'polkachu.com'
 when b.validator_from = 'cosmosvaloper1083svrca4t350mphfv9x45wq9asrs60cdmrflj' then 'Notional'
 when b.validator_from = 'cosmosvaloper1nuhls0wyf8slhmuasha5pz0u89jrf9nnugq8ak' then 'Golden Ratio Staking'
 when b.validator_from = 'cosmosvaloper1x8rr4hcf54nz6hfckyy2n05sxss54h8wz9puzg' then 'cosmosgbt'
 when b.validator_from = 'cosmosvaloper1thl5syhmscgnj7whdyrydw3w6vy80044hjpnxh' then 'RockawayX Infra'
 when b.validator_from = 'cosmosvaloper1keltez56g3zm9w8wr8gcmmulze48g2q3usuw8c' then 'DeFi Wallet'
 when b.validator_from = 'cosmosvaloper140l6y2gp3gxvay6qtn70re7z2s0gn57zfd832j' then 'Lavender.Five Nodes 🐝'
 when b.validator_from = 'cosmosvaloper1ddle9tczl87gsvmeva3c48nenyng4n56nghmjk' then 'Witval'
 when b.validator_from = 'cosmosvaloper1rwh0cxa72d3yle3r4l8gd7vyphrmjy2kpe4x72' then 'pe4x72'
 when b.validator_from = 'cosmosvaloper19ecn7ljwp6el2pc5lldyauwv05ufwut9mm38r5' then 'WhisperNode'
 when b.validator_from = 'cosmosvaloper1fhr7e04ct0zslmkzqt9smakg3sxrdve6ulclj2' then 'Stakin'
 when b.validator_from = 'cosmosvaloper1jlr62guqwrwkdt4m3y00zh2rrsamhjf9num5xr' then 'StakeWithUs'
 when b.validator_from = 'cosmosvaloper122j3zmqdl6d2g64qmjuqzj65gfejsvjp07yljn' then 'COS_Validator'
 when b.validator_from = 'cosmosvaloper1xym2qygmr9vanpa0m7ndk3n0qxgey3ffzcyd5c' then '🐡grant.fish'
 when b.validator_from = 'cosmosvaloper1e4vye322gkjx8n85jgcclnc7nvdvu82axnr5ll' then 'Binary Holdings'
 when b.validator_from = 'cosmosvaloper13maqgtlklmereflvg3lq3e8zrp0jsqhr8ef3kk' then 'ChainUp'
 when b.validator_from = 'cosmosvaloper1kn3wugetjuy4zetlq6wadchfhvu3x740ae6z6x' then 'Huobi'
 when b.validator_from = 'cosmosvaloper1svwt2mr4x2mx0hcmty0mxsa4rmlfau4lwx2l69' then 'Twinstake-Validator'
 when b.validator_from = 'cosmosvaloper1wrx0x9m9ykdhw9sg04v7uljme53wuj03aa5d4f' then 'Just-Mining'
 when b.validator_from = 'cosmosvaloper16yupepagywvlk7uhpfchtwa0stu5f8cyhh54f2' then 'Stakely.io'
 when b.validator_from = 'cosmosvaloper18extdhzzl5c8tr6453e5hzaj3exrdlea90fj3y' then 'Smart Stake'
 when b.validator_from = 'cosmosvaloper1e859xaue4k2jzqw20cv6l7p3tmc378pc3k8g2u' then 'Citizen Cosmos'
 when b.validator_from = 'cosmosvaloper1rcp29q3hpd246n6qak7jluqep4v006cdsc2kkl' then 'in3s.com'
 when b.validator_from = 'cosmosvaloper1vygmh344ldv9qefss9ek7ggsnxparljlmj56q5' then 'PUPMØS'
 when b.validator_from = 'cosmosvaloper16s96n9k9zztdgjy8q4qcxp4hn7ww98qkrka4zk' then 'Oni '
 when b.validator_from = 'cosmosvaloper1wqy2s6nwnxj57l0l5rdjxxr646p3al6y70435m' then 'Klub Staking'
 when b.validator_from = 'cosmosvaloper1xnrth5rku3z3msm9prxe3l0p2yec3d9mzxz9ka' then 'coinhall.org'
 when b.validator_from = 'cosmosvaloper102ruvpv2srmunfffxavttxnhezln6fnc54at8c' then 'Ztake.org'
 when b.validator_from = 'cosmosvaloper1fsg635n5vgc7jazz9sx5725wnc3xqgr7awxaag' then 'cros-nest'
 when b.validator_from = 'cosmosvaloper1xwazl8ftks4gn00y5x3c47auquc62ssuqlj02r' then 'jabbey'
 when b.validator_from = 'cosmosvaloper1e0plfg475phrsvrlzw8gwppeva0zk5yg9fgg8c' then 'Easy 2 Stake'
 when b.validator_from = 'cosmosvaloper10unx6s0cdqntvrumd5hs07rgd5ytcztqh8etw6' then 'GATA DAO'
 when b.validator_from = 'cosmosvaloper1fqzqejwkk898fcslw4z4eeqjzesynvrdfr5hte' then 'commercio.network'
 when b.validator_from = 'cosmosvaloper142w8q2l0gxsfna72gq8t7e4ee4ul37e9htgtxx' then 'NEOPLY'
 when b.validator_from = 'cosmosvaloper1jmykcq8gylmy5tgqtel4xj4q62fdt49sl584xd' then 'Blocks United | blocksunited.com'
 when b.validator_from = 'cosmosvaloper16qme5yxucnaj6snx35nmwze0wyxr8wfgqxsqfw' then 'KIRA Staking'
 when b.validator_from = 'cosmosvaloper1aewyh4gtvayx6v7w592jdfylawk4rsu9tfvfgm' then 'Silk Nodes'
 when b.validator_from = 'cosmosvaloper125umsz3fws7gepn5ccsh0sv4gre9r6a3tccz4r' then 'Moonstake'
 when b.validator_from = 'cosmosvaloper14qazscc80zgzx3m0m0aa30ths0p9hg8vdglqrc' then 'CryptoCrew Validators ✅'
 when b.validator_from = 'cosmosvaloper1et77usu8q2hargvyusl4qzryev8x8t9wwqkxfs' then 'Stargaze'
 when b.validator_from = 'cosmosvaloper1485u80fdxjan4sd3esrvyw6cyurpvddvzuh48y' then 'AIR DROP STATION'
 when b.validator_from = 'cosmosvaloper1yw5s259jkcg0jzmh7sce29uk0lqqw2ump7578p' then 'CEX.IO'
 when b.validator_from = 'cosmosvaloper1lkujuk2004p3w42tgvuvqnsdmsq8u6jqkwf9wj' then 'BitValidator'
 when b.validator_from = 'cosmosvaloper140e7u946a2nqqkvcnjpjm83d0ynsqem8dnp684' then 'danku_zone w/ DAIC'
 when b.validator_from = 'cosmosvaloper13x77yexvf6qexfjg9czp6jhpv7vpjdwwkyhe4p' then 'blockscape'
 when b.validator_from = 'cosmosvaloper1jxv0u20scum4trha72c7ltfgfqef6nsch7q6cu' then 'Ping'
 when b.validator_from = 'cosmosvaloper1qs8tnw2t8l6amtzvdemnnsq9dzk0ag0z52uzay' then 'Castlenode'
 when b.validator_from = 'cosmosvaloper1z66j0z75a9flwnez7sa8jxx46cqu4rfhd9q82w' then 'debo-validator'
 when b.validator_from = 'cosmosvaloper1648ynlpdw7fqa2axt0w2yp3fk542junl7rsvq6' then 'Any Labs'
 when b.validator_from = 'cosmosvaloper1j0vaeh27t4rll7zhmarwcuq8xtrmvqhudrgcky' then 'Chainflow'
 when b.validator_from = 'cosmosvaloper1v69lzl909kje64k8vae24uytpxcnpxgullz2dx' then 'Terra Nodes'
 when b.validator_from = 'cosmosvaloper103agss48504gkk3la5xcg5kxplaf6ttnuv234h' then 'MANTRA DAO'
 when b.validator_from = 'cosmosvaloper1sdz4rc95vnzh2f54sacec50vjxnmwdakfym4vh' then 'Chill Validation'
 when b.validator_from = 'cosmosvaloper12lfqufkk2h3w2ycp50czme6nj3ln5tdv7nj3hx' then 'Fanfury | fury.fan | Stake to Win'
 when b.validator_from = 'cosmosvaloper1crqm3598z6qmyn2kkcl9dz7uqs4qdqnr6s8jdn' then 'Coinbase Cloud'
 when b.validator_from = 'cosmosvaloper1ukpah0340rx7k3x2njnavwyjv6pfpvn632df9q' then 'IcyCRO '
 when b.validator_from = 'cosmosvaloper1ualhu3fjgg77g485gmyswkq3w0dp7gys6qzwrv' then 'stake.systems'
 when b.validator_from = 'cosmosvaloper13ql36flc4cdjhx08hke5vpr4dyv03aafnmvtnc' then 'TienThuatToan Capital'
 when b.validator_from = 'cosmosvaloper1urxrvt5dmkqpe50gwrerjly2z6nvk9exjz2j3h' then 'zoomerlabs'
 when b.validator_from = 'cosmosvaloper1ff0dw8kawsnxkrgj7p65kvw7jxxakyf8n583gx' then 'Compass'
 when b.validator_from = 'cosmosvaloper1v78emy9d2xe3tj974l7tmn2whca2nh9zp7s0u9' then 'a41'
 when b.validator_from = 'cosmosvaloper1kyfce0nvluyhgfsdzz8hwrsf5336gsc95pyy4u' then 'StakeSeeker by BTCS'
 when b.validator_from = 'cosmosvaloper1ed5a27kfyu0yljmna00vtr8mgzp6rwh9zn77zz' then 'CROSSTECH'
 when b.validator_from = 'cosmosvaloper1usvshtypjw57edkwxq3tagme665398f0hf4wuc' then 'Made In Block'
 when b.validator_from = 'cosmosvaloper1ha8d55747h8hsaluvz8ld88n24nfaw68rx4x92' then 'Lightning Capital'
 when b.validator_from = 'cosmosvaloper1wlpz5hau2ezu0gmuxav63m53d8s77az9wfzlt6' then '🤑 uGaenn ⛅'
 when b.validator_from = 'cosmosvaloper1zc0z44e42qhzltqc8qpj5qrzn836d3lftnqmgw' then 'Virtual Hive'
 when b.validator_from = 'cosmosvaloper1rj6324uq904z5zr96zg6ew9qjyau9u6h5nflg6' then 'Don Cryptonium'
 when b.validator_from = 'cosmosvaloper1yh089p0cre4nhpdqw35uzde5amg3qzexkeggdn' then 'High Stakes 🇨🇭'
 when b.validator_from = 'cosmosvaloper1a4qlael79p76my9pml6thwhnnzsxyy4ajrvd9s' then 'Multiplex'
 when b.validator_from = 'cosmosvaloper14upntdx8lf0f49t987mj99zksxnluanvu6x4lu' then 'Republic Crypto'
 when b.validator_from = 'cosmosvaloper1x3mkgqpshvpq87d33ndsleu7gd7w47dl4ve0yy' then 'CrowdControl'
 when b.validator_from = 'cosmosvaloper10f9wkd6vdspac05djyfwfx0uxcqxapnqhnkcg8' then 'Tavis Digital'
 when b.validator_from = 'cosmosvaloper1yfnaup5wa3vdzx3wx9auhvzl85saqj37tqxqnu' then 'Moonlet'
 when b.validator_from = 'cosmosvaloper1wdrypwex63geqswmcy5qynv4w3z3dyef2qmyna' then 'Genesis Lab'
 when b.validator_from = 'cosmosvaloper1de7qx00pz2j6gn9k88ntxxylelkazfk3g8fgh9' then 'Cosmic Validator | Auto-compound'
 when b.validator_from = 'cosmosvaloper1nxe3gnztx8wvayj260dp6yw7jg797m8up02h7z' then 'Synclub'
 when b.validator_from = 'cosmosvaloper1u6ddcsjueax884l3tfrs66497c7g86skn7pa0u' then 'Sentinel'
 when b.validator_from = 'cosmosvaloper1ec3p6a75mqwkv33zt543n6cnxqwun37rr5xlqv' then 'lunamint'
 when b.validator_from = 'cosmosvaloper1fun809ksxh87nzf88yashp9ynjz6xkscrtvzvw' then 'Tessellated'
 when b.validator_from = 'cosmosvaloper1gf3dm2mvqhymts6ksrstlyuu2m8pw6dhfp9md2' then 'Blockapsis'
 when b.validator_from = 'cosmosvaloper15r4tc0m6hc7z8drq3dzlrtcs6rq2q9l2nvwher' then 'DragonStake'
 when b.validator_from = 'cosmosvaloper1nz3c4q40j8jyvg2hcljkwhe69872mnllf7v9xh' then 'Interstellar Lounge'
 when b.validator_from = 'cosmosvaloper106yp7zw35wftheyyv9f9pe69t8rteumjrx52jg' then 'Bro_n_Bro'
 when b.validator_from = 'cosmosvaloper1v0g7guekttkdmerz5z8hjj8u8j68c6p00zqgf5' then 'LUNC DAO'
 when b.validator_from = 'cosmosvaloper12w6tynmjzq4l8zdla3v4x0jt8lt4rcz5gk7zg2' then 'Huobi-1'
 when b.validator_from = 'cosmosvaloper1d0aup392g3enru7eash83sedqclaxvp7fzh6gk' then 'Stir'
 when b.validator_from = 'cosmosvaloper1s05va5d09xlq3et8mapsesqh6r5lqy7mkhwshm' then 'Wetez'
 when b.validator_from = 'cosmosvaloper1n3nll7yl3lcv932s2r7l6jzvkjtjk0qppp3rls' then 'RoundTable21 by WildSage Labs'
  else 'Other' end as from_validator, 

 case when validator_to = 'cosmosvaloper1sjllsnramtg3ewxqwwrwjxfgc4n4ef9u2lcnj0' then 'Stake fish '
 when validator_to = 'cosmosvaloper1c4k24jzduc365kywrsvf5ujz4ya6mwympnc4en' then 'Coinbase Custody'
 when validator_to = 'cosmosvaloper14lultfckehtszvzw4ehu0apvsr77afvyju5zzy' then 'DokiaCapital'
 when validator_to = 'cosmosvaloper1v5y0tg0jllvxf5c3afml8s3awue0ymju89frut' then 'Zero Knowledge Validator (ZKV)'
 when validator_to = 'cosmosvaloper196ax4vc0lwpxndu9dyhvca7jhxp70rmcvrj90c' then 'SG-1'
 when validator_to = 'cosmosvaloper18ruzecmqj9pv8ac0gvkgryuc7u004te9rh7w5s' then 'Binance node'
 when validator_to = 'cosmosvaloper14k4pzckkre6uxxyd2lnhnpp8sngys9m6hl6ml7' then 'Polychain'
 when validator_to = 'cosmosvaloper1tflk30mq5vgqjdly92kkhhq3raev2hnz6eete3' then 'Everstake'
 when validator_to = 'cosmosvaloper1qaa9zej9a0ge3ugpx3pxyx602lxh3ztqgfnp42' then 'Game'
 when validator_to = 'cosmosvaloper19lss6zgdh5vvcpjhfftdghrpsw7a4434elpwpu' then 'Paradigm'
 when validator_to = 'cosmosvaloper1ey69r37gfxvxg62sh4r0ktpuc46pzjrm873ae8' then 'Sika'
 when validator_to = 'cosmosvaloper1hjct6q7npsspsg3dgvzk3sdf89spmlpfdn6m9d' then 'Figment'
 when validator_to = 'cosmosvaloper1clpqr4nrk4khgkxj78fcwwh6dl3uw4epsluffn' then 'Cosmostation'
 when validator_to = 'cosmosvaloper156gqf9837u7d4c4678yt3rl4ls9c5vuursrrzf' then 'Binance staking'
 when validator_to = 'cosmosvaloper132juzk0gdmwuxvx4phug7m3ymyatxlh9734g4w' then 'P2P.org'
 when validator_to = 'cosmosvaloper15urq2dtp9qce4fyc85m6upwm9xul3049e02707' then 'Chorus One'
 when validator_to = 'cosmosvaloper1z8zjv3lntpwxua0rtpvgrcwl0nm0tltgpgs6l7' then 'Kraken'
 when validator_to = 'cosmosvaloper1vf44d85es37hwl9f4h9gv0e064m0lla60j9luj' then 'Multichain ventures'
 when validator_to = 'cosmosvaloper16k579jk6yt2cwmqx9dz5xvq9fug2tekvlu9qdv' then 'Informal systems'
 when validator_to = 'cosmosvaloper1zqgheeawp7cmqk27dgyctd80rd8ryhqs6la9wc' then 'No fee to 2025'
 when validator_to = 'cosmosvaloper1g48268mu5vfp4wk7dk89r0wdrakm9p5xk0q50k' then 'Provalidator'
 when validator_to = 'cosmosvaloper1lzhlnpahvznwfv4jmay2tgaha5kmz5qxerarrl' then 'Citadel.one'
 when validator_to = 'cosmosvaloper1gpx52r9h3zeul45amvcy2pysgvcwddxrgx6cnv' then 'StakeLab'
 when validator_to = 'cosmosvaloper1qwl879nx9t6kef4supyazayf7vjhennyh568ys' then 'Certus One'
 when validator_to = 'cosmosvaloper1gdg6qqe5a3u483unqlqsnullja23g0xvqkxtk0' then 'Zugerselfdelegation'
 when validator_to = 'cosmosvaloper1n229vhepft6wnkt5tjpwmxdmcnfz55jv3vp77d' then 'Allnodes.com'
 when validator_to = 'cosmosvaloper1ma02nlc7lchu7caufyrrqt4r6v2mpsj90y9wzd' then 'Hashtower'
 when validator_to = 'cosmosvaloper1vvwtk805lxehwle9l4yudmq6mn0g32px9xtkhc' then 'Imperator.co'
 when validator_to = 'cosmosvaloper1eh5mwu044gd5ntkkc2xgfg8247mgc56fz4sdg3' then 'Boubounode'
 when validator_to = 'cosmosvaloper1grgelyng2v6v3t8z87wu3sxgt9m5s03xfytvz7' then 'Inqlusion'
 when validator_to = 'cosmosvaloper1te8nxpc2myjfrhaty0dnzdhs5ahdh5agzuym9v' then 'CoinoneNode'
 when validator_to = 'cosmosvaloper1rpgtz9pskr5geavkjz02caqmeep7cwwpv73axj' then 'Blockpower'
 when validator_to = 'cosmosvaloper14kn0kk33szpwus9nh8n87fjel8djx0y070ymmj' then 'Forbole'
 when validator_to = 'cosmosvaloper1y0us8xvsvfvqkk9c6nt5cfyu5au5tww2ztve7q' then 'Swiss Staking'
 when validator_to = 'cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p' then 'Staking Facilities'
 when validator_to = 'cosmosvaloper130mdu9a0etmeuw52qfxk73pn0ga6gawkxsrlwf' then 'strangelove-ventures'
 when validator_to = 'cosmosvaloper16fnz0v4cnv5dpnj0p3gaft2q2kzx8z5hfrx6v5' then 'DACM'
 when validator_to = 'cosmosvaloper1we6knm8qartmmh2r0qfpsz6pq0s7emv3e0meuw' then 'Staked'
 when validator_to = 'cosmosvaloper1jst8q8flpn94u9uvkpae8mrkk3a5pjhxx529z2' then 'Node Guardians'
 when validator_to = 'cosmosvaloper10e4vsut6suau8tk9m6dnrm0slgd6npe3jx5xpv' then 'B-Harvest'
 when validator_to = 'cosmosvaloper1kgddca7qj96z0qcxr2c45z73cfl0c75p7f3s2e' then 'ChainLayer'
 when validator_to = 'cosmosvaloper1cc99d3xcukhedg4wcw53j7a9q68uza707vpfe7' then 'dForce'
 when validator_to = 'cosmosvaloper19rmlxkqjt950fxl849l49x0me56u9tkd5n5j62' then 'Post Road'
 when validator_to = 'cosmosvaloper199mlc7fr6ll5t54w7tts7f4s0cvnqgc59nmuxf' then 'ShapeShift DAO'
 when validator_to = 'cosmosvaloper1k2d9ed9vgfuk2m58a2d80q9u6qljkh4vfaqjfq' then 'Stakecito'
 when validator_to = 'cosmosvaloper10wljxpl03053h9690apmyeakly3ylhejrucvtm' then 'Ledger'
 when validator_to = 'cosmosvaloper1uutuwrwt3z2a5z8z3uasml3rftlpmu25aga5c6' then 'DelegaNetworks '
 when validator_to = 'cosmosvaloper1ssm0d433seakyak8kcf93yefhknjleeds4y3em' then 'IRISnet-Bianjie'
 when validator_to = 'cosmosvaloper1ehkfl7palwrh6w2hhr2yfrgrq8jetgucudztfe' then 'KalpaTech'
 when validator_to = 'cosmosvaloper19yy989ka5usws6gsd8vl94y7l6ssgdwsrnscjc' then 'OKEx Pool'
 when validator_to = 'cosmosvaloper1hjadhj9nqzpye2vkmkz4thahhd0z8dh3udhq74' then 'Atomic Nodes'
 when validator_to = 'cosmosvaloper157v7tczs40axfgejp2m43kwuzqe0wsy0rv8puv' then 'POSTHUMAN DVS'
 when validator_to = 'cosmosvaloper1gxju9ky3hwxvqqagrl3dxtl49kjpxq6wlqe6m5' then 'Vortex.live'
 when validator_to = 'cosmosvaloper1n3mhyp9fvcmuu8l0q8qvjy07x0rql8q46fe2xk' then '0base.vc'
 when validator_to = 'cosmosvaloper146kwpzhmleafmhtaxulfptyhnvwxzlvm87hwnm' then 'KysenPool Sky'
 when validator_to = 'cosmosvaloper1x8efhljzvs52u5xa6m7crcwes7v9u0nlwdgw30' then 'Upbit Staking'
 when validator_to = 'cosmosvaloper14l0fp639yudfl46zauvv8rkzjgd4u0zk2aseys' then 'ATEAM'
 when validator_to = 'cosmosvaloper13nvnv6q8d3yg7tjeahjzljkqu0y27s8y9e7as9' then 'Latent Iron'
 when validator_to = 'cosmosvaloper1dqp325was50l7ut2lnx6s8xhmtwj3wrtx06gzu' then 'Nocturnal Labs'
 when validator_to = 'cosmosvaloper1lktjhnzkpkz3ehrg8psvmwhafg56kfss3q3t8m' then 'Umbrella '
 when validator_to = 'cosmosvaloper1udpsgkgyutgsglauk9vk9rs03a3skc62gup9ny' then 'AUDIT.one'
 when validator_to = 'cosmosvaloper10nzaaeh2kq28t3nqsh5m8kmyv90vx7ym5mpakx' then 'Blockdaemon'
 when validator_to = 'cosmosvaloper1sd4tl9aljmmezzudugs7zlaya7pg2895ws8tfs' then 'InfStones'
 when validator_to = 'cosmosvaloper124maqmcqv8tquy764ktz7cu0gxnzfw54n3vww8' then 'Simply Staking'
 when validator_to = 'cosmosvaloper1uhnsxv6m83jj3328mhrql7yax3nge5svrv6t6c' then 'S16 Research Ventures'
 when validator_to = 'cosmosvaloper1ptyzewnns2kn37ewtmv6ppsvhdnmeapvtfc9y5' then 'WeStaking'
 when validator_to = 'cosmosvaloper157qezau9xnzypse3vu2vhs7r4ee83fdecew0fz' then 'KuCoin'
 when validator_to = 'cosmosvaloper1ul2me6vukg2vac2p6ltxmqlaa7jywdgt8q76ag' then 'HyperblocksPro'
 when validator_to = 'cosmosvaloper17mggn4znyeyg25wd7498qxl7r2jhgue8u4qjcq' then '01node'
 when validator_to = 'cosmosvaloper1q6d3d089hg59x6gcx92uumx70s5y5wadklue8s' then 'Ubik Capital 0%Fee'
 when validator_to = 'cosmosvaloper1sxx9mszve0gaedz5ld7qdkjkfv8z992ax69k08' then 'e-Money.com // validator.network'
 when validator_to = 'cosmosvaloper1lcwxu50rvvgf9v6jy6q5mrzyhlszwtjxhtscmp' then 'stakezone'
 when validator_to = 'cosmosvaloper1dt93l3qgmhhlp97srjyqyendrgu9nx0suxtwe8' then '天照☀'
 when validator_to = 'cosmosvaloper1ej2es5fjztqjcd4pwa0zyvaevtjd2y5wxxp9gd' then 'Frens '
 when validator_to = 'cosmosvaloper1gjtvly9lel6zskvwtvlg5vhwpu9c9waw7sxzwx' then 'EZStaking.io'
 when validator_to = 'cosmosvaloper1r2dthxctqzhwg299e7aaeqwfkgcc9hg8k3yd7m' then '0% Fee 🌻 Sunflower'
 when validator_to = 'cosmosvaloper1pjmngrwcsatsuyy8m3qrunaun67sr9x7z5r2qs' then 'Cypher Core'
 when validator_to = 'cosmosvaloper10jzj3jjd3frna0ay08sh4zu4fpy957s49jkk7m' then 'Onbloc Node'
 when validator_to = 'cosmosvaloper1m73mgwn3cm2e8x9a9axa0kw8nqz8a492ms63vn' then '#decentralizehk - DHK dao'
 when validator_to = 'cosmosvaloper1symf474wnypes2d3mecllqk6l26rwz8mfjqdus' then 'BlockHunters '
 when validator_to = 'cosmosvaloper1hdrlqvyjfy5sdrseecjrutyws9khtxxaux62l7' then 'SmartNodes'
 when validator_to = 'cosmosvaloper17h2x3j7u44qkrq0sk8ul0r2qr440rwgjkfg0gh' then 'FreshATOMS.com'
 when validator_to = 'cosmosvaloper1gf4wlkutql95j7wwsxz490s6fahlvk2s9xpwax' then 'Stakewolle.com | Auto-compound'
 when validator_to = 'cosmosvaloper1cgh5ksjwy2sd407lyre4l3uj2fdrqhpkzp06e6' then 'HashQuark'
 when validator_to = 'cosmosvaloper13sduv92y3xdhy3rpmhakrc3v7t37e7ps9l0kpv' then 'nylira.net'
 when validator_to = 'cosmosvaloper1gp957czryfgyvxwn3tfnyy2f0t9g2p4pqeemx8' then 'polkachu.com'
 when validator_to = 'cosmosvaloper1083svrca4t350mphfv9x45wq9asrs60cdmrflj' then 'Notional'
 when validator_to = 'cosmosvaloper1nuhls0wyf8slhmuasha5pz0u89jrf9nnugq8ak' then 'Golden Ratio Staking'
 when validator_to = 'cosmosvaloper1x8rr4hcf54nz6hfckyy2n05sxss54h8wz9puzg' then 'cosmosgbt'
 when validator_to = 'cosmosvaloper1thl5syhmscgnj7whdyrydw3w6vy80044hjpnxh' then 'RockawayX Infra'
 when validator_to = 'cosmosvaloper1keltez56g3zm9w8wr8gcmmulze48g2q3usuw8c' then 'DeFi Wallet'
 when validator_to = 'cosmosvaloper140l6y2gp3gxvay6qtn70re7z2s0gn57zfd832j' then 'Lavender.Five Nodes 🐝'
 when validator_to = 'cosmosvaloper1ddle9tczl87gsvmeva3c48nenyng4n56nghmjk' then 'Witval'
 when validator_to = 'cosmosvaloper1rwh0cxa72d3yle3r4l8gd7vyphrmjy2kpe4x72' then 'pe4x72'
 when validator_to = 'cosmosvaloper19ecn7ljwp6el2pc5lldyauwv05ufwut9mm38r5' then 'WhisperNode'
 when validator_to = 'cosmosvaloper1fhr7e04ct0zslmkzqt9smakg3sxrdve6ulclj2' then 'Stakin'
 when validator_to = 'cosmosvaloper1jlr62guqwrwkdt4m3y00zh2rrsamhjf9num5xr' then 'StakeWithUs'
 when validator_to = 'cosmosvaloper122j3zmqdl6d2g64qmjuqzj65gfejsvjp07yljn' then 'COS_Validator'
 when validator_to = 'cosmosvaloper1xym2qygmr9vanpa0m7ndk3n0qxgey3ffzcyd5c' then '🐡grant.fish'
 when validator_to = 'cosmosvaloper1e4vye322gkjx8n85jgcclnc7nvdvu82axnr5ll' then 'Binary Holdings'
 when validator_to = 'cosmosvaloper13maqgtlklmereflvg3lq3e8zrp0jsqhr8ef3kk' then 'ChainUp'
 when validator_to = 'cosmosvaloper1kn3wugetjuy4zetlq6wadchfhvu3x740ae6z6x' then 'Huobi'
 when validator_to = 'cosmosvaloper1svwt2mr4x2mx0hcmty0mxsa4rmlfau4lwx2l69' then 'Twinstake-Validator'
 when validator_to = 'cosmosvaloper1wrx0x9m9ykdhw9sg04v7uljme53wuj03aa5d4f' then 'Just-Mining'
 when validator_to = 'cosmosvaloper16yupepagywvlk7uhpfchtwa0stu5f8cyhh54f2' then 'Stakely.io'
 when validator_to = 'cosmosvaloper18extdhzzl5c8tr6453e5hzaj3exrdlea90fj3y' then 'Smart Stake'
 when validator_to = 'cosmosvaloper1e859xaue4k2jzqw20cv6l7p3tmc378pc3k8g2u' then 'Citizen Cosmos'
 when validator_to = 'cosmosvaloper1rcp29q3hpd246n6qak7jluqep4v006cdsc2kkl' then 'in3s.com'
 when validator_to = 'cosmosvaloper1vygmh344ldv9qefss9ek7ggsnxparljlmj56q5' then 'PUPMØS'
 when validator_to = 'cosmosvaloper16s96n9k9zztdgjy8q4qcxp4hn7ww98qkrka4zk' then 'Oni '
 when validator_to = 'cosmosvaloper1wqy2s6nwnxj57l0l5rdjxxr646p3al6y70435m' then 'Klub Staking'
 when validator_to = 'cosmosvaloper1xnrth5rku3z3msm9prxe3l0p2yec3d9mzxz9ka' then 'coinhall.org'
 when validator_to = 'cosmosvaloper102ruvpv2srmunfffxavttxnhezln6fnc54at8c' then 'Ztake.org'
 when validator_to = 'cosmosvaloper1fsg635n5vgc7jazz9sx5725wnc3xqgr7awxaag' then 'cros-nest'
 when validator_to = 'cosmosvaloper1xwazl8ftks4gn00y5x3c47auquc62ssuqlj02r' then 'jabbey'
 when validator_to = 'cosmosvaloper1e0plfg475phrsvrlzw8gwppeva0zk5yg9fgg8c' then 'Easy 2 Stake'
 when validator_to = 'cosmosvaloper10unx6s0cdqntvrumd5hs07rgd5ytcztqh8etw6' then 'GATA DAO'
 when validator_to = 'cosmosvaloper1fqzqejwkk898fcslw4z4eeqjzesynvrdfr5hte' then 'commercio.network'
 when validator_to = 'cosmosvaloper142w8q2l0gxsfna72gq8t7e4ee4ul37e9htgtxx' then 'NEOPLY'
 when validator_to = 'cosmosvaloper1jmykcq8gylmy5tgqtel4xj4q62fdt49sl584xd' then 'Blocks United | blocksunited.com'
 when validator_to = 'cosmosvaloper16qme5yxucnaj6snx35nmwze0wyxr8wfgqxsqfw' then 'KIRA Staking'
 when validator_to = 'cosmosvaloper1aewyh4gtvayx6v7w592jdfylawk4rsu9tfvfgm' then 'Silk Nodes'
 when validator_to = 'cosmosvaloper125umsz3fws7gepn5ccsh0sv4gre9r6a3tccz4r' then 'Moonstake'
 when validator_to = 'cosmosvaloper14qazscc80zgzx3m0m0aa30ths0p9hg8vdglqrc' then 'CryptoCrew Validators ✅'
 when validator_to = 'cosmosvaloper1et77usu8q2hargvyusl4qzryev8x8t9wwqkxfs' then 'Stargaze'
 when validator_to = 'cosmosvaloper1485u80fdxjan4sd3esrvyw6cyurpvddvzuh48y' then 'AIR DROP STATION'
 when validator_to = 'cosmosvaloper1yw5s259jkcg0jzmh7sce29uk0lqqw2ump7578p' then 'CEX.IO'
 when validator_to = 'cosmosvaloper1lkujuk2004p3w42tgvuvqnsdmsq8u6jqkwf9wj' then 'BitValidator'
 when validator_to = 'cosmosvaloper140e7u946a2nqqkvcnjpjm83d0ynsqem8dnp684' then 'danku_zone w/ DAIC'
 when validator_to = 'cosmosvaloper13x77yexvf6qexfjg9czp6jhpv7vpjdwwkyhe4p' then 'blockscape'
 when validator_to = 'cosmosvaloper1jxv0u20scum4trha72c7ltfgfqef6nsch7q6cu' then 'Ping'
 when validator_to = 'cosmosvaloper1qs8tnw2t8l6amtzvdemnnsq9dzk0ag0z52uzay' then 'Castlenode'
 when validator_to = 'cosmosvaloper1z66j0z75a9flwnez7sa8jxx46cqu4rfhd9q82w' then 'debo-validator'
 when validator_to = 'cosmosvaloper1648ynlpdw7fqa2axt0w2yp3fk542junl7rsvq6' then 'Any Labs'
 when validator_to = 'cosmosvaloper1j0vaeh27t4rll7zhmarwcuq8xtrmvqhudrgcky' then 'Chainflow'
 when validator_to = 'cosmosvaloper1v69lzl909kje64k8vae24uytpxcnpxgullz2dx' then 'Terra Nodes'
 when validator_to = 'cosmosvaloper103agss48504gkk3la5xcg5kxplaf6ttnuv234h' then 'MANTRA DAO'
 when validator_to = 'cosmosvaloper1sdz4rc95vnzh2f54sacec50vjxnmwdakfym4vh' then 'Chill Validation'
 when validator_to = 'cosmosvaloper12lfqufkk2h3w2ycp50czme6nj3ln5tdv7nj3hx' then 'Fanfury | fury.fan | Stake to Win'
 when validator_to = 'cosmosvaloper1crqm3598z6qmyn2kkcl9dz7uqs4qdqnr6s8jdn' then 'Coinbase Cloud'
 when validator_to = 'cosmosvaloper1ukpah0340rx7k3x2njnavwyjv6pfpvn632df9q' then 'IcyCRO '
 when validator_to = 'cosmosvaloper1ualhu3fjgg77g485gmyswkq3w0dp7gys6qzwrv' then 'stake.systems'
 when validator_to = 'cosmosvaloper13ql36flc4cdjhx08hke5vpr4dyv03aafnmvtnc' then 'TienThuatToan Capital'
 when validator_to = 'cosmosvaloper1urxrvt5dmkqpe50gwrerjly2z6nvk9exjz2j3h' then 'zoomerlabs'
 when validator_to = 'cosmosvaloper1ff0dw8kawsnxkrgj7p65kvw7jxxakyf8n583gx' then 'Compass'
 when validator_to = 'cosmosvaloper1v78emy9d2xe3tj974l7tmn2whca2nh9zp7s0u9' then 'a41'
 when validator_to = 'cosmosvaloper1kyfce0nvluyhgfsdzz8hwrsf5336gsc95pyy4u' then 'StakeSeeker by BTCS'
 when validator_to = 'cosmosvaloper1ed5a27kfyu0yljmna00vtr8mgzp6rwh9zn77zz' then 'CROSSTECH'
 when validator_to = 'cosmosvaloper1usvshtypjw57edkwxq3tagme665398f0hf4wuc' then 'Made In Block'
 when validator_to = 'cosmosvaloper1ha8d55747h8hsaluvz8ld88n24nfaw68rx4x92' then 'Lightning Capital'
 when validator_to = 'cosmosvaloper1wlpz5hau2ezu0gmuxav63m53d8s77az9wfzlt6' then '🤑 uGaenn ⛅'
 when validator_to = 'cosmosvaloper1zc0z44e42qhzltqc8qpj5qrzn836d3lftnqmgw' then 'Virtual Hive'
 when validator_to = 'cosmosvaloper1rj6324uq904z5zr96zg6ew9qjyau9u6h5nflg6' then 'Don Cryptonium'
 when validator_to = 'cosmosvaloper1yh089p0cre4nhpdqw35uzde5amg3qzexkeggdn' then 'High Stakes 🇨🇭'
 when validator_to = 'cosmosvaloper1a4qlael79p76my9pml6thwhnnzsxyy4ajrvd9s' then 'Multiplex'
 when validator_to = 'cosmosvaloper14upntdx8lf0f49t987mj99zksxnluanvu6x4lu' then 'Republic Crypto'
 when validator_to = 'cosmosvaloper1x3mkgqpshvpq87d33ndsleu7gd7w47dl4ve0yy' then 'CrowdControl'
 when validator_to = 'cosmosvaloper10f9wkd6vdspac05djyfwfx0uxcqxapnqhnkcg8' then 'Tavis Digital'
 when validator_to = 'cosmosvaloper1yfnaup5wa3vdzx3wx9auhvzl85saqj37tqxqnu' then 'Moonlet'
 when validator_to = 'cosmosvaloper1wdrypwex63geqswmcy5qynv4w3z3dyef2qmyna' then 'Genesis Lab'
 when validator_to = 'cosmosvaloper1de7qx00pz2j6gn9k88ntxxylelkazfk3g8fgh9' then 'Cosmic Validator | Auto-compound'
 when validator_to = 'cosmosvaloper1nxe3gnztx8wvayj260dp6yw7jg797m8up02h7z' then 'Synclub'
 when validator_to = 'cosmosvaloper1u6ddcsjueax884l3tfrs66497c7g86skn7pa0u' then 'Sentinel'
 when validator_to = 'cosmosvaloper1ec3p6a75mqwkv33zt543n6cnxqwun37rr5xlqv' then 'lunamint'
 when validator_to = 'cosmosvaloper1fun809ksxh87nzf88yashp9ynjz6xkscrtvzvw' then 'Tessellated'
 when validator_to = 'cosmosvaloper1gf3dm2mvqhymts6ksrstlyuu2m8pw6dhfp9md2' then 'Blockapsis'
 when validator_to = 'cosmosvaloper15r4tc0m6hc7z8drq3dzlrtcs6rq2q9l2nvwher' then 'DragonStake'
 when validator_to = 'cosmosvaloper1nz3c4q40j8jyvg2hcljkwhe69872mnllf7v9xh' then 'Interstellar Lounge'
 when validator_to = 'cosmosvaloper106yp7zw35wftheyyv9f9pe69t8rteumjrx52jg' then 'Bro_n_Bro'
 when validator_to = 'cosmosvaloper1v0g7guekttkdmerz5z8hjj8u8j68c6p00zqgf5' then 'LUNC DAO'
 when validator_to = 'cosmosvaloper12w6tynmjzq4l8zdla3v4x0jt8lt4rcz5gk7zg2' then 'Huobi-1'
 when validator_to = 'cosmosvaloper1d0aup392g3enru7eash83sedqclaxvp7fzh6gk' then 'Stir'
 when validator_to = 'cosmosvaloper1s05va5d09xlq3et8mapsesqh6r5lqy7mkhwshm' then 'Wetez'
 when validator_to = 'cosmosvaloper1n3nll7yl3lcv932s2r7l6jzvkjtjk0qppp3rls' then 'RoundTable21 by WildSage Labs'
else 'Other' end as to_validator,
    case when validator_from = 'cosmosvaloper1sjllsnramtg3ewxqwwrwjxfgc4n4ef9u2lcnj0' then '1'
when validator_from = 'cosmosvaloper1c4k24jzduc365kywrsvf5ujz4ya6mwympnc4en' then '2'
when validator_from = 'cosmosvaloper14lultfckehtszvzw4ehu0apvsr77afvyju5zzy' then '3'
when validator_from = 'cosmosvaloper1v5y0tg0jllvxf5c3afml8s3awue0ymju89frut' then '4'
when validator_from = 'cosmosvaloper196ax4vc0lwpxndu9dyhvca7jhxp70rmcvrj90c' then '5'
when validator_from = 'cosmosvaloper18ruzecmqj9pv8ac0gvkgryuc7u004te9rh7w5s' then '6'
when validator_from = 'cosmosvaloper14k4pzckkre6uxxyd2lnhnpp8sngys9m6hl6ml7' then '7'
when validator_from = 'cosmosvaloper1tflk30mq5vgqjdly92kkhhq3raev2hnz6eete3' then '8'
when validator_from = 'cosmosvaloper1qaa9zej9a0ge3ugpx3pxyx602lxh3ztqgfnp42' then '9'
when validator_from = 'cosmosvaloper19lss6zgdh5vvcpjhfftdghrpsw7a4434elpwpu' then '10'
when validator_from = 'cosmosvaloper1ey69r37gfxvxg62sh4r0ktpuc46pzjrm873ae8' then '11'
when validator_from = 'cosmosvaloper1hjct6q7npsspsg3dgvzk3sdf89spmlpfdn6m9d' then '12'
when validator_from = 'cosmosvaloper1clpqr4nrk4khgkxj78fcwwh6dl3uw4epsluffn' then '13'
when validator_from = 'cosmosvaloper156gqf9837u7d4c4678yt3rl4ls9c5vuursrrzf' then '14'
when validator_from = 'cosmosvaloper132juzk0gdmwuxvx4phug7m3ymyatxlh9734g4w' then '15'
when validator_from = 'cosmosvaloper15urq2dtp9qce4fyc85m6upwm9xul3049e02707' then '16'
when validator_from = 'cosmosvaloper1z8zjv3lntpwxua0rtpvgrcwl0nm0tltgpgs6l7' then '17'
when validator_from = 'cosmosvaloper1vf44d85es37hwl9f4h9gv0e064m0lla60j9luj' then '18'
when validator_from = 'cosmosvaloper16k579jk6yt2cwmqx9dz5xvq9fug2tekvlu9qdv' then '19'
when validator_from = 'cosmosvaloper1zqgheeawp7cmqk27dgyctd80rd8ryhqs6la9wc' then '20'
when validator_from = 'cosmosvaloper1g48268mu5vfp4wk7dk89r0wdrakm9p5xk0q50k' then '21'
when validator_from = 'cosmosvaloper1lzhlnpahvznwfv4jmay2tgaha5kmz5qxerarrl' then '22'
when validator_from = 'cosmosvaloper1gpx52r9h3zeul45amvcy2pysgvcwddxrgx6cnv' then '23'
when validator_from = 'cosmosvaloper1qwl879nx9t6kef4supyazayf7vjhennyh568ys' then '24'
when validator_from = 'cosmosvaloper1gdg6qqe5a3u483unqlqsnullja23g0xvqkxtk0' then '25'
when validator_from = 'cosmosvaloper1n229vhepft6wnkt5tjpwmxdmcnfz55jv3vp77d' then '26'
when validator_from = 'cosmosvaloper1ma02nlc7lchu7caufyrrqt4r6v2mpsj90y9wzd' then '27'
when validator_from = 'cosmosvaloper1vvwtk805lxehwle9l4yudmq6mn0g32px9xtkhc' then '28'
when validator_from = 'cosmosvaloper1eh5mwu044gd5ntkkc2xgfg8247mgc56fz4sdg3' then '29'
when validator_from = 'cosmosvaloper1grgelyng2v6v3t8z87wu3sxgt9m5s03xfytvz7' then '30'
when validator_from = 'cosmosvaloper1te8nxpc2myjfrhaty0dnzdhs5ahdh5agzuym9v' then '31'
when validator_from = 'cosmosvaloper1rpgtz9pskr5geavkjz02caqmeep7cwwpv73axj' then '32'
when validator_from = 'cosmosvaloper14kn0kk33szpwus9nh8n87fjel8djx0y070ymmj' then '33'
when validator_from = 'cosmosvaloper1y0us8xvsvfvqkk9c6nt5cfyu5au5tww2ztve7q' then '34'
when validator_from = 'cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p' then '35'
when validator_from = 'cosmosvaloper130mdu9a0etmeuw52qfxk73pn0ga6gawkxsrlwf' then '36'
when validator_from = 'cosmosvaloper16fnz0v4cnv5dpnj0p3gaft2q2kzx8z5hfrx6v5' then '37'
when validator_from = 'cosmosvaloper1we6knm8qartmmh2r0qfpsz6pq0s7emv3e0meuw' then '38'
when validator_from = 'cosmosvaloper1jst8q8flpn94u9uvkpae8mrkk3a5pjhxx529z2' then '39'
when validator_from = 'cosmosvaloper10e4vsut6suau8tk9m6dnrm0slgd6npe3jx5xpv' then '40'
when validator_from = 'cosmosvaloper1kgddca7qj96z0qcxr2c45z73cfl0c75p7f3s2e' then '41'
when validator_from = 'cosmosvaloper1cc99d3xcukhedg4wcw53j7a9q68uza707vpfe7' then '42'
when validator_from = 'cosmosvaloper19rmlxkqjt950fxl849l49x0me56u9tkd5n5j62' then '43'
when validator_from = 'cosmosvaloper199mlc7fr6ll5t54w7tts7f4s0cvnqgc59nmuxf' then '44'
when validator_from = 'cosmosvaloper1k2d9ed9vgfuk2m58a2d80q9u6qljkh4vfaqjfq' then '45'
when validator_from = 'cosmosvaloper10wljxpl03053h9690apmyeakly3ylhejrucvtm' then '46'
when validator_from = 'cosmosvaloper1uutuwrwt3z2a5z8z3uasml3rftlpmu25aga5c6' then '47'
when validator_from = 'cosmosvaloper1ssm0d433seakyak8kcf93yefhknjleeds4y3em' then '48'
when validator_from = 'cosmosvaloper1ehkfl7palwrh6w2hhr2yfrgrq8jetgucudztfe' then '49'
when validator_from = 'cosmosvaloper19yy989ka5usws6gsd8vl94y7l6ssgdwsrnscjc' then '50'
when validator_from = 'cosmosvaloper1hjadhj9nqzpye2vkmkz4thahhd0z8dh3udhq74' then '51'
when validator_from = 'cosmosvaloper157v7tczs40axfgejp2m43kwuzqe0wsy0rv8puv' then '52'
when validator_from = 'cosmosvaloper1gxju9ky3hwxvqqagrl3dxtl49kjpxq6wlqe6m5' then '53'
when validator_from = 'cosmosvaloper1n3mhyp9fvcmuu8l0q8qvjy07x0rql8q46fe2xk' then '54'
when validator_from = 'cosmosvaloper146kwpzhmleafmhtaxulfptyhnvwxzlvm87hwnm' then '55'
when validator_from = 'cosmosvaloper1x8efhljzvs52u5xa6m7crcwes7v9u0nlwdgw30' then '56'
when validator_from = 'cosmosvaloper14l0fp639yudfl46zauvv8rkzjgd4u0zk2aseys' then '57'
when validator_from = 'cosmosvaloper13nvnv6q8d3yg7tjeahjzljkqu0y27s8y9e7as9' then '58'
when validator_from = 'cosmosvaloper1dqp325was50l7ut2lnx6s8xhmtwj3wrtx06gzu' then '59'
when validator_from = 'cosmosvaloper1lktjhnzkpkz3ehrg8psvmwhafg56kfss3q3t8m' then '60'
when validator_from = 'cosmosvaloper1udpsgkgyutgsglauk9vk9rs03a3skc62gup9ny' then '61'
when validator_from = 'cosmosvaloper10nzaaeh2kq28t3nqsh5m8kmyv90vx7ym5mpakx' then '62'
when validator_from = 'cosmosvaloper1sd4tl9aljmmezzudugs7zlaya7pg2895ws8tfs' then '63'
when validator_from = 'cosmosvaloper124maqmcqv8tquy764ktz7cu0gxnzfw54n3vww8' then '64'
when validator_from = 'cosmosvaloper1uhnsxv6m83jj3328mhrql7yax3nge5svrv6t6c' then '65'
when validator_from = 'cosmosvaloper1ptyzewnns2kn37ewtmv6ppsvhdnmeapvtfc9y5' then '66'
when validator_from = 'cosmosvaloper157qezau9xnzypse3vu2vhs7r4ee83fdecew0fz' then '67'
when validator_from = 'cosmosvaloper1ul2me6vukg2vac2p6ltxmqlaa7jywdgt8q76ag' then '68'
when validator_from = 'cosmosvaloper17mggn4znyeyg25wd7498qxl7r2jhgue8u4qjcq' then '69'
when validator_from = 'cosmosvaloper1q6d3d089hg59x6gcx92uumx70s5y5wadklue8s' then '70'
when validator_from = 'cosmosvaloper1sxx9mszve0gaedz5ld7qdkjkfv8z992ax69k08' then '71'
when validator_from = 'cosmosvaloper1lcwxu50rvvgf9v6jy6q5mrzyhlszwtjxhtscmp' then '72'
when validator_from = 'cosmosvaloper1dt93l3qgmhhlp97srjyqyendrgu9nx0suxtwe8' then '73'
when validator_from = 'cosmosvaloper1ej2es5fjztqjcd4pwa0zyvaevtjd2y5wxxp9gd' then '74'
when validator_from = 'cosmosvaloper1gjtvly9lel6zskvwtvlg5vhwpu9c9waw7sxzwx' then '75'
when validator_from = 'cosmosvaloper1r2dthxctqzhwg299e7aaeqwfkgcc9hg8k3yd7m' then '76'
when validator_from = 'cosmosvaloper1pjmngrwcsatsuyy8m3qrunaun67sr9x7z5r2qs' then '77'
when validator_from = 'cosmosvaloper10jzj3jjd3frna0ay08sh4zu4fpy957s49jkk7m' then '78'
when validator_from = 'cosmosvaloper1m73mgwn3cm2e8x9a9axa0kw8nqz8a492ms63vn' then '79'
when validator_from = 'cosmosvaloper1symf474wnypes2d3mecllqk6l26rwz8mfjqdus' then '80'
when validator_from = 'cosmosvaloper1hdrlqvyjfy5sdrseecjrutyws9khtxxaux62l7' then '81'
when validator_from = 'cosmosvaloper17h2x3j7u44qkrq0sk8ul0r2qr440rwgjkfg0gh' then '82'
when validator_from = 'cosmosvaloper1gf4wlkutql95j7wwsxz490s6fahlvk2s9xpwax' then '83'
when validator_from = 'cosmosvaloper1cgh5ksjwy2sd407lyre4l3uj2fdrqhpkzp06e6' then '84'
when validator_from = 'cosmosvaloper13sduv92y3xdhy3rpmhakrc3v7t37e7ps9l0kpv' then '85'
when validator_from = 'cosmosvaloper1gp957czryfgyvxwn3tfnyy2f0t9g2p4pqeemx8' then '86'
when validator_from = 'cosmosvaloper1083svrca4t350mphfv9x45wq9asrs60cdmrflj' then '87'
when validator_from = 'cosmosvaloper1nuhls0wyf8slhmuasha5pz0u89jrf9nnugq8ak' then '88'
when validator_from = 'cosmosvaloper1x8rr4hcf54nz6hfckyy2n05sxss54h8wz9puzg' then '89'
when validator_from = 'cosmosvaloper1thl5syhmscgnj7whdyrydw3w6vy80044hjpnxh' then '90'
when validator_from = 'cosmosvaloper1keltez56g3zm9w8wr8gcmmulze48g2q3usuw8c' then '91'
when validator_from = 'cosmosvaloper140l6y2gp3gxvay6qtn70re7z2s0gn57zfd832j' then '92'
when validator_from = 'cosmosvaloper1ddle9tczl87gsvmeva3c48nenyng4n56nghmjk' then '93'
when validator_from = 'cosmosvaloper1rwh0cxa72d3yle3r4l8gd7vyphrmjy2kpe4x72' then '94'
when validator_from = 'cosmosvaloper19ecn7ljwp6el2pc5lldyauwv05ufwut9mm38r5' then '95'
when validator_from = 'cosmosvaloper1fhr7e04ct0zslmkzqt9smakg3sxrdve6ulclj2' then '96'
when validator_from = 'cosmosvaloper1jlr62guqwrwkdt4m3y00zh2rrsamhjf9num5xr' then '97'
when validator_from = 'cosmosvaloper122j3zmqdl6d2g64qmjuqzj65gfejsvjp07yljn' then '98'
when validator_from = 'cosmosvaloper1xym2qygmr9vanpa0m7ndk3n0qxgey3ffzcyd5c' then '99'
when validator_from = 'cosmosvaloper1e4vye322gkjx8n85jgcclnc7nvdvu82axnr5ll' then '100'
when validator_from = 'cosmosvaloper13maqgtlklmereflvg3lq3e8zrp0jsqhr8ef3kk' then '101'
when validator_from = 'cosmosvaloper1kn3wugetjuy4zetlq6wadchfhvu3x740ae6z6x' then '102'
when validator_from = 'cosmosvaloper1svwt2mr4x2mx0hcmty0mxsa4rmlfau4lwx2l69' then '103'
when validator_from = 'cosmosvaloper1wrx0x9m9ykdhw9sg04v7uljme53wuj03aa5d4f' then '104'
when validator_from = 'cosmosvaloper16yupepagywvlk7uhpfchtwa0stu5f8cyhh54f2' then '105'
when validator_from = 'cosmosvaloper18extdhzzl5c8tr6453e5hzaj3exrdlea90fj3y' then '106'
when validator_from = 'cosmosvaloper1e859xaue4k2jzqw20cv6l7p3tmc378pc3k8g2u' then '107'
when validator_from = 'cosmosvaloper1rcp29q3hpd246n6qak7jluqep4v006cdsc2kkl' then '108'
when validator_from = 'cosmosvaloper1vygmh344ldv9qefss9ek7ggsnxparljlmj56q5' then '109'
when validator_from = 'cosmosvaloper16s96n9k9zztdgjy8q4qcxp4hn7ww98qkrka4zk' then '110'
when validator_from = 'cosmosvaloper1wqy2s6nwnxj57l0l5rdjxxr646p3al6y70435m' then '111'
when validator_from = 'cosmosvaloper1xnrth5rku3z3msm9prxe3l0p2yec3d9mzxz9ka' then '112'
when validator_from = 'cosmosvaloper102ruvpv2srmunfffxavttxnhezln6fnc54at8c' then '113'
when validator_from = 'cosmosvaloper1fsg635n5vgc7jazz9sx5725wnc3xqgr7awxaag' then '114'
when validator_from = 'cosmosvaloper1xwazl8ftks4gn00y5x3c47auquc62ssuqlj02r' then '115'
when validator_from = 'cosmosvaloper1e0plfg475phrsvrlzw8gwppeva0zk5yg9fgg8c' then '116'
when validator_from = 'cosmosvaloper10unx6s0cdqntvrumd5hs07rgd5ytcztqh8etw6' then '117'
when validator_from = 'cosmosvaloper1fqzqejwkk898fcslw4z4eeqjzesynvrdfr5hte' then '118'
when validator_from = 'cosmosvaloper142w8q2l0gxsfna72gq8t7e4ee4ul37e9htgtxx' then '119'
when validator_from = 'cosmosvaloper1jmykcq8gylmy5tgqtel4xj4q62fdt49sl584xd' then '120'
when validator_from = 'cosmosvaloper16qme5yxucnaj6snx35nmwze0wyxr8wfgqxsqfw' then '121'
when validator_from = 'cosmosvaloper1aewyh4gtvayx6v7w592jdfylawk4rsu9tfvfgm' then '122'
when validator_from = 'cosmosvaloper125umsz3fws7gepn5ccsh0sv4gre9r6a3tccz4r' then '123'
when validator_from = 'cosmosvaloper14qazscc80zgzx3m0m0aa30ths0p9hg8vdglqrc' then '124'
when validator_from = 'cosmosvaloper1et77usu8q2hargvyusl4qzryev8x8t9wwqkxfs' then '125'
when validator_from = 'cosmosvaloper1485u80fdxjan4sd3esrvyw6cyurpvddvzuh48y' then '126'
when validator_from = 'cosmosvaloper1yw5s259jkcg0jzmh7sce29uk0lqqw2ump7578p' then '127'
when validator_from = 'cosmosvaloper1lkujuk2004p3w42tgvuvqnsdmsq8u6jqkwf9wj' then '128'
when validator_from = 'cosmosvaloper140e7u946a2nqqkvcnjpjm83d0ynsqem8dnp684' then '129'
when validator_from = 'cosmosvaloper13x77yexvf6qexfjg9czp6jhpv7vpjdwwkyhe4p' then '130'
when validator_from = 'cosmosvaloper1jxv0u20scum4trha72c7ltfgfqef6nsch7q6cu' then '131'
when validator_from = 'cosmosvaloper1qs8tnw2t8l6amtzvdemnnsq9dzk0ag0z52uzay' then '132'
when validator_from = 'cosmosvaloper1z66j0z75a9flwnez7sa8jxx46cqu4rfhd9q82w' then '133'
when validator_from = 'cosmosvaloper1648ynlpdw7fqa2axt0w2yp3fk542junl7rsvq6' then '134'
when validator_from = 'cosmosvaloper1j0vaeh27t4rll7zhmarwcuq8xtrmvqhudrgcky' then '135'
when validator_from = 'cosmosvaloper1v69lzl909kje64k8vae24uytpxcnpxgullz2dx' then '136'
when validator_from = 'cosmosvaloper103agss48504gkk3la5xcg5kxplaf6ttnuv234h' then '137'
when validator_from = 'cosmosvaloper1sdz4rc95vnzh2f54sacec50vjxnmwdakfym4vh' then '138'
when validator_from = 'cosmosvaloper12lfqufkk2h3w2ycp50czme6nj3ln5tdv7nj3hx' then '139'
when validator_from = 'cosmosvaloper1crqm3598z6qmyn2kkcl9dz7uqs4qdqnr6s8jdn' then '140'
when validator_from = 'cosmosvaloper1ukpah0340rx7k3x2njnavwyjv6pfpvn632df9q' then '141'
when validator_from = 'cosmosvaloper1ualhu3fjgg77g485gmyswkq3w0dp7gys6qzwrv' then '142'
when validator_from = 'cosmosvaloper13ql36flc4cdjhx08hke5vpr4dyv03aafnmvtnc' then '143'
when validator_from = 'cosmosvaloper1urxrvt5dmkqpe50gwrerjly2z6nvk9exjz2j3h' then '144'
when validator_from = 'cosmosvaloper1ff0dw8kawsnxkrgj7p65kvw7jxxakyf8n583gx' then '145'
when validator_from = 'cosmosvaloper1v78emy9d2xe3tj974l7tmn2whca2nh9zp7s0u9' then '146'
when validator_from = 'cosmosvaloper1kyfce0nvluyhgfsdzz8hwrsf5336gsc95pyy4u' then '147'
when validator_from = 'cosmosvaloper1ed5a27kfyu0yljmna00vtr8mgzp6rwh9zn77zz' then '148'
when validator_from = 'cosmosvaloper1usvshtypjw57edkwxq3tagme665398f0hf4wuc' then '149'
when validator_from = 'cosmosvaloper1ha8d55747h8hsaluvz8ld88n24nfaw68rx4x92' then '150'
when validator_from = 'cosmosvaloper1wlpz5hau2ezu0gmuxav63m53d8s77az9wfzlt6' then '151'
when validator_from = 'cosmosvaloper1zc0z44e42qhzltqc8qpj5qrzn836d3lftnqmgw' then '152'
when validator_from = 'cosmosvaloper1rj6324uq904z5zr96zg6ew9qjyau9u6h5nflg6' then '153'
when validator_from = 'cosmosvaloper1yh089p0cre4nhpdqw35uzde5amg3qzexkeggdn' then '154'
when validator_from = 'cosmosvaloper1a4qlael79p76my9pml6thwhnnzsxyy4ajrvd9s' then '155'
when validator_from = 'cosmosvaloper14upntdx8lf0f49t987mj99zksxnluanvu6x4lu' then '156'
when validator_from = 'cosmosvaloper1x3mkgqpshvpq87d33ndsleu7gd7w47dl4ve0yy' then '157'
when validator_from = 'cosmosvaloper10f9wkd6vdspac05djyfwfx0uxcqxapnqhnkcg8' then '158'
when validator_from = 'cosmosvaloper1yfnaup5wa3vdzx3wx9auhvzl85saqj37tqxqnu' then '159'
when validator_from = 'cosmosvaloper1wdrypwex63geqswmcy5qynv4w3z3dyef2qmyna' then '160'
when validator_from = 'cosmosvaloper1de7qx00pz2j6gn9k88ntxxylelkazfk3g8fgh9' then '161'
when validator_from = 'cosmosvaloper1nxe3gnztx8wvayj260dp6yw7jg797m8up02h7z' then '162'
when validator_from = 'cosmosvaloper1u6ddcsjueax884l3tfrs66497c7g86skn7pa0u' then '163'
when validator_from = 'cosmosvaloper1ec3p6a75mqwkv33zt543n6cnxqwun37rr5xlqv' then '164'
when validator_from = 'cosmosvaloper1fun809ksxh87nzf88yashp9ynjz6xkscrtvzvw' then '165'
when validator_from = 'cosmosvaloper1gf3dm2mvqhymts6ksrstlyuu2m8pw6dhfp9md2' then '166'
when validator_from = 'cosmosvaloper15r4tc0m6hc7z8drq3dzlrtcs6rq2q9l2nvwher' then '167'
when validator_from = 'cosmosvaloper1nz3c4q40j8jyvg2hcljkwhe69872mnllf7v9xh' then '168'
when validator_from = 'cosmosvaloper106yp7zw35wftheyyv9f9pe69t8rteumjrx52jg' then '169'
when validator_from = 'cosmosvaloper1v0g7guekttkdmerz5z8hjj8u8j68c6p00zqgf5' then '170'
when validator_from = 'cosmosvaloper12w6tynmjzq4l8zdla3v4x0jt8lt4rcz5gk7zg2' then '171'
when validator_from = 'cosmosvaloper1d0aup392g3enru7eash83sedqclaxvp7fzh6gk' then '172'
when validator_from = 'cosmosvaloper1s05va5d09xlq3et8mapsesqh6r5lqy7mkhwshm' then '173'
when validator_from = 'cosmosvaloper1n3nll7yl3lcv932s2r7l6jzvkjtjk0qppp3rls' then '174'
else '200' end as from_validator_rank,
  
case when c.validator_to = 'cosmosvaloper1sjllsnramtg3ewxqwwrwjxfgc4n4ef9u2lcnj0' then '1'
when c.validator_to = 'cosmosvaloper1c4k24jzduc365kywrsvf5ujz4ya6mwympnc4en' then '2'
when c.validator_to = 'cosmosvaloper14lultfckehtszvzw4ehu0apvsr77afvyju5zzy' then '3'
when c.validator_to = 'cosmosvaloper1v5y0tg0jllvxf5c3afml8s3awue0ymju89frut' then '4'
when c.validator_to = 'cosmosvaloper196ax4vc0lwpxndu9dyhvca7jhxp70rmcvrj90c' then '5'
when c.validator_to = 'cosmosvaloper18ruzecmqj9pv8ac0gvkgryuc7u004te9rh7w5s' then '6'
when c.validator_to = 'cosmosvaloper14k4pzckkre6uxxyd2lnhnpp8sngys9m6hl6ml7' then '7'
when c.validator_to = 'cosmosvaloper1tflk30mq5vgqjdly92kkhhq3raev2hnz6eete3' then '8'
when c.validator_to = 'cosmosvaloper1qaa9zej9a0ge3ugpx3pxyx602lxh3ztqgfnp42' then '9'
when c.validator_to = 'cosmosvaloper19lss6zgdh5vvcpjhfftdghrpsw7a4434elpwpu' then '10'
when c.validator_to = 'cosmosvaloper1ey69r37gfxvxg62sh4r0ktpuc46pzjrm873ae8' then '11'
when c.validator_to = 'cosmosvaloper1hjct6q7npsspsg3dgvzk3sdf89spmlpfdn6m9d' then '12'
when c.validator_to = 'cosmosvaloper1clpqr4nrk4khgkxj78fcwwh6dl3uw4epsluffn' then '13'
when c.validator_to = 'cosmosvaloper156gqf9837u7d4c4678yt3rl4ls9c5vuursrrzf' then '14'
when c.validator_to = 'cosmosvaloper132juzk0gdmwuxvx4phug7m3ymyatxlh9734g4w' then '15'
when c.validator_to = 'cosmosvaloper15urq2dtp9qce4fyc85m6upwm9xul3049e02707' then '16'
when c.validator_to = 'cosmosvaloper1z8zjv3lntpwxua0rtpvgrcwl0nm0tltgpgs6l7' then '17'
when c.validator_to = 'cosmosvaloper1vf44d85es37hwl9f4h9gv0e064m0lla60j9luj' then '18'
when c.validator_to = 'cosmosvaloper16k579jk6yt2cwmqx9dz5xvq9fug2tekvlu9qdv' then '19'
when c.validator_to = 'cosmosvaloper1zqgheeawp7cmqk27dgyctd80rd8ryhqs6la9wc' then '20'
when c.validator_to = 'cosmosvaloper1g48268mu5vfp4wk7dk89r0wdrakm9p5xk0q50k' then '21'
when c.validator_to = 'cosmosvaloper1lzhlnpahvznwfv4jmay2tgaha5kmz5qxerarrl' then '22'
when c.validator_to = 'cosmosvaloper1gpx52r9h3zeul45amvcy2pysgvcwddxrgx6cnv' then '23'
when c.validator_to = 'cosmosvaloper1qwl879nx9t6kef4supyazayf7vjhennyh568ys' then '24'
when c.validator_to = 'cosmosvaloper1gdg6qqe5a3u483unqlqsnullja23g0xvqkxtk0' then '25'
when c.validator_to = 'cosmosvaloper1n229vhepft6wnkt5tjpwmxdmcnfz55jv3vp77d' then '26'
when c.validator_to = 'cosmosvaloper1ma02nlc7lchu7caufyrrqt4r6v2mpsj90y9wzd' then '27'
when c.validator_to = 'cosmosvaloper1vvwtk805lxehwle9l4yudmq6mn0g32px9xtkhc' then '28'
when c.validator_to = 'cosmosvaloper1eh5mwu044gd5ntkkc2xgfg8247mgc56fz4sdg3' then '29'
when c.validator_to = 'cosmosvaloper1grgelyng2v6v3t8z87wu3sxgt9m5s03xfytvz7' then '30'
when c.validator_to = 'cosmosvaloper1te8nxpc2myjfrhaty0dnzdhs5ahdh5agzuym9v' then '31'
when c.validator_to = 'cosmosvaloper1rpgtz9pskr5geavkjz02caqmeep7cwwpv73axj' then '32'
when c.validator_to = 'cosmosvaloper14kn0kk33szpwus9nh8n87fjel8djx0y070ymmj' then '33'
when c.validator_to = 'cosmosvaloper1y0us8xvsvfvqkk9c6nt5cfyu5au5tww2ztve7q' then '34'
when c.validator_to = 'cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p' then '35'
when c.validator_to = 'cosmosvaloper130mdu9a0etmeuw52qfxk73pn0ga6gawkxsrlwf' then '36'
when c.validator_to = 'cosmosvaloper16fnz0v4cnv5dpnj0p3gaft2q2kzx8z5hfrx6v5' then '37'
when c.validator_to = 'cosmosvaloper1we6knm8qartmmh2r0qfpsz6pq0s7emv3e0meuw' then '38'
when c.validator_to = 'cosmosvaloper1jst8q8flpn94u9uvkpae8mrkk3a5pjhxx529z2' then '39'
when c.validator_to = 'cosmosvaloper10e4vsut6suau8tk9m6dnrm0slgd6npe3jx5xpv' then '40'
when c.validator_to = 'cosmosvaloper1kgddca7qj96z0qcxr2c45z73cfl0c75p7f3s2e' then '41'
when c.validator_to = 'cosmosvaloper1cc99d3xcukhedg4wcw53j7a9q68uza707vpfe7' then '42'
when c.validator_to = 'cosmosvaloper19rmlxkqjt950fxl849l49x0me56u9tkd5n5j62' then '43'
when c.validator_to = 'cosmosvaloper199mlc7fr6ll5t54w7tts7f4s0cvnqgc59nmuxf' then '44'
when c.validator_to = 'cosmosvaloper1k2d9ed9vgfuk2m58a2d80q9u6qljkh4vfaqjfq' then '45'
when c.validator_to = 'cosmosvaloper10wljxpl03053h9690apmyeakly3ylhejrucvtm' then '46'
when c.validator_to = 'cosmosvaloper1uutuwrwt3z2a5z8z3uasml3rftlpmu25aga5c6' then '47'
when c.validator_to = 'cosmosvaloper1ssm0d433seakyak8kcf93yefhknjleeds4y3em' then '48'
when c.validator_to = 'cosmosvaloper1ehkfl7palwrh6w2hhr2yfrgrq8jetgucudztfe' then '49'
when c.validator_to = 'cosmosvaloper19yy989ka5usws6gsd8vl94y7l6ssgdwsrnscjc' then '50'
when c.validator_to = 'cosmosvaloper1hjadhj9nqzpye2vkmkz4thahhd0z8dh3udhq74' then '51'
when c.validator_to = 'cosmosvaloper157v7tczs40axfgejp2m43kwuzqe0wsy0rv8puv' then '52'
when c.validator_to = 'cosmosvaloper1gxju9ky3hwxvqqagrl3dxtl49kjpxq6wlqe6m5' then '53'
when c.validator_to = 'cosmosvaloper1n3mhyp9fvcmuu8l0q8qvjy07x0rql8q46fe2xk' then '54'
when c.validator_to = 'cosmosvaloper146kwpzhmleafmhtaxulfptyhnvwxzlvm87hwnm' then '55'
when c.validator_to = 'cosmosvaloper1x8efhljzvs52u5xa6m7crcwes7v9u0nlwdgw30' then '56'
when c.validator_to = 'cosmosvaloper14l0fp639yudfl46zauvv8rkzjgd4u0zk2aseys' then '57'
when c.validator_to = 'cosmosvaloper13nvnv6q8d3yg7tjeahjzljkqu0y27s8y9e7as9' then '58'
when c.validator_to = 'cosmosvaloper1dqp325was50l7ut2lnx6s8xhmtwj3wrtx06gzu' then '59'
when c.validator_to = 'cosmosvaloper1lktjhnzkpkz3ehrg8psvmwhafg56kfss3q3t8m' then '60'
when c.validator_to = 'cosmosvaloper1udpsgkgyutgsglauk9vk9rs03a3skc62gup9ny' then '61'
when c.validator_to = 'cosmosvaloper10nzaaeh2kq28t3nqsh5m8kmyv90vx7ym5mpakx' then '62'
when c.validator_to = 'cosmosvaloper1sd4tl9aljmmezzudugs7zlaya7pg2895ws8tfs' then '63'
when c.validator_to = 'cosmosvaloper124maqmcqv8tquy764ktz7cu0gxnzfw54n3vww8' then '64'
when c.validator_to = 'cosmosvaloper1uhnsxv6m83jj3328mhrql7yax3nge5svrv6t6c' then '65'
when c.validator_to = 'cosmosvaloper1ptyzewnns2kn37ewtmv6ppsvhdnmeapvtfc9y5' then '66'
when c.validator_to = 'cosmosvaloper157qezau9xnzypse3vu2vhs7r4ee83fdecew0fz' then '67'
when c.validator_to = 'cosmosvaloper1ul2me6vukg2vac2p6ltxmqlaa7jywdgt8q76ag' then '68'
when c.validator_to = 'cosmosvaloper17mggn4znyeyg25wd7498qxl7r2jhgue8u4qjcq' then '69'
when c.validator_to = 'cosmosvaloper1q6d3d089hg59x6gcx92uumx70s5y5wadklue8s' then '70'
when c.validator_to = 'cosmosvaloper1sxx9mszve0gaedz5ld7qdkjkfv8z992ax69k08' then '71'
when c.validator_to = 'cosmosvaloper1lcwxu50rvvgf9v6jy6q5mrzyhlszwtjxhtscmp' then '72'
when c.validator_to = 'cosmosvaloper1dt93l3qgmhhlp97srjyqyendrgu9nx0suxtwe8' then '73'
when c.validator_to = 'cosmosvaloper1ej2es5fjztqjcd4pwa0zyvaevtjd2y5wxxp9gd' then '74'
when c.validator_to = 'cosmosvaloper1gjtvly9lel6zskvwtvlg5vhwpu9c9waw7sxzwx' then '75'
when c.validator_to = 'cosmosvaloper1r2dthxctqzhwg299e7aaeqwfkgcc9hg8k3yd7m' then '76'
when c.validator_to = 'cosmosvaloper1pjmngrwcsatsuyy8m3qrunaun67sr9x7z5r2qs' then '77'
when c.validator_to = 'cosmosvaloper10jzj3jjd3frna0ay08sh4zu4fpy957s49jkk7m' then '78'
when c.validator_to = 'cosmosvaloper1m73mgwn3cm2e8x9a9axa0kw8nqz8a492ms63vn' then '79'
when c.validator_to = 'cosmosvaloper1symf474wnypes2d3mecllqk6l26rwz8mfjqdus' then '80'
when c.validator_to = 'cosmosvaloper1hdrlqvyjfy5sdrseecjrutyws9khtxxaux62l7' then '81'
when c.validator_to = 'cosmosvaloper17h2x3j7u44qkrq0sk8ul0r2qr440rwgjkfg0gh' then '82'
when c.validator_to = 'cosmosvaloper1gf4wlkutql95j7wwsxz490s6fahlvk2s9xpwax' then '83'
when c.validator_to = 'cosmosvaloper1cgh5ksjwy2sd407lyre4l3uj2fdrqhpkzp06e6' then '84'
when c.validator_to = 'cosmosvaloper13sduv92y3xdhy3rpmhakrc3v7t37e7ps9l0kpv' then '85'
when c.validator_to = 'cosmosvaloper1gp957czryfgyvxwn3tfnyy2f0t9g2p4pqeemx8' then '86'
when c.validator_to = 'cosmosvaloper1083svrca4t350mphfv9x45wq9asrs60cdmrflj' then '87'
when c.validator_to = 'cosmosvaloper1nuhls0wyf8slhmuasha5pz0u89jrf9nnugq8ak' then '88'
when c.validator_to = 'cosmosvaloper1x8rr4hcf54nz6hfckyy2n05sxss54h8wz9puzg' then '89'
when c.validator_to = 'cosmosvaloper1thl5syhmscgnj7whdyrydw3w6vy80044hjpnxh' then '90'
when c.validator_to = 'cosmosvaloper1keltez56g3zm9w8wr8gcmmulze48g2q3usuw8c' then '91'
when c.validator_to = 'cosmosvaloper140l6y2gp3gxvay6qtn70re7z2s0gn57zfd832j' then '92'
when c.validator_to = 'cosmosvaloper1ddle9tczl87gsvmeva3c48nenyng4n56nghmjk' then '93'
when c.validator_to = 'cosmosvaloper1rwh0cxa72d3yle3r4l8gd7vyphrmjy2kpe4x72' then '94'
when c.validator_to = 'cosmosvaloper19ecn7ljwp6el2pc5lldyauwv05ufwut9mm38r5' then '95'
when c.validator_to = 'cosmosvaloper1fhr7e04ct0zslmkzqt9smakg3sxrdve6ulclj2' then '96'
when c.validator_to = 'cosmosvaloper1jlr62guqwrwkdt4m3y00zh2rrsamhjf9num5xr' then '97'
when c.validator_to = 'cosmosvaloper122j3zmqdl6d2g64qmjuqzj65gfejsvjp07yljn' then '98'
when c.validator_to = 'cosmosvaloper1xym2qygmr9vanpa0m7ndk3n0qxgey3ffzcyd5c' then '99'
when c.validator_to = 'cosmosvaloper1e4vye322gkjx8n85jgcclnc7nvdvu82axnr5ll' then '100'
when c.validator_to = 'cosmosvaloper13maqgtlklmereflvg3lq3e8zrp0jsqhr8ef3kk' then '101'
when c.validator_to = 'cosmosvaloper1kn3wugetjuy4zetlq6wadchfhvu3x740ae6z6x' then '102'
when c.validator_to = 'cosmosvaloper1svwt2mr4x2mx0hcmty0mxsa4rmlfau4lwx2l69' then '103'
when c.validator_to = 'cosmosvaloper1wrx0x9m9ykdhw9sg04v7uljme53wuj03aa5d4f' then '104'
when c.validator_to = 'cosmosvaloper16yupepagywvlk7uhpfchtwa0stu5f8cyhh54f2' then '105'
when c.validator_to = 'cosmosvaloper18extdhzzl5c8tr6453e5hzaj3exrdlea90fj3y' then '106'
when c.validator_to = 'cosmosvaloper1e859xaue4k2jzqw20cv6l7p3tmc378pc3k8g2u' then '107'
when c.validator_to = 'cosmosvaloper1rcp29q3hpd246n6qak7jluqep4v006cdsc2kkl' then '108'
when c.validator_to = 'cosmosvaloper1vygmh344ldv9qefss9ek7ggsnxparljlmj56q5' then '109'
when c.validator_to = 'cosmosvaloper16s96n9k9zztdgjy8q4qcxp4hn7ww98qkrka4zk' then '110'
when c.validator_to = 'cosmosvaloper1wqy2s6nwnxj57l0l5rdjxxr646p3al6y70435m' then '111'
when c.validator_to = 'cosmosvaloper1xnrth5rku3z3msm9prxe3l0p2yec3d9mzxz9ka' then '112'
when c.validator_to = 'cosmosvaloper102ruvpv2srmunfffxavttxnhezln6fnc54at8c' then '113'
when c.validator_to = 'cosmosvaloper1fsg635n5vgc7jazz9sx5725wnc3xqgr7awxaag' then '114'
when c.validator_to = 'cosmosvaloper1xwazl8ftks4gn00y5x3c47auquc62ssuqlj02r' then '115'
when c.validator_to = 'cosmosvaloper1e0plfg475phrsvrlzw8gwppeva0zk5yg9fgg8c' then '116'
when c.validator_to = 'cosmosvaloper10unx6s0cdqntvrumd5hs07rgd5ytcztqh8etw6' then '117'
when c.validator_to = 'cosmosvaloper1fqzqejwkk898fcslw4z4eeqjzesynvrdfr5hte' then '118'
when c.validator_to = 'cosmosvaloper142w8q2l0gxsfna72gq8t7e4ee4ul37e9htgtxx' then '119'
when c.validator_to = 'cosmosvaloper1jmykcq8gylmy5tgqtel4xj4q62fdt49sl584xd' then '120'
when c.validator_to = 'cosmosvaloper16qme5yxucnaj6snx35nmwze0wyxr8wfgqxsqfw' then '121'
when c.validator_to = 'cosmosvaloper1aewyh4gtvayx6v7w592jdfylawk4rsu9tfvfgm' then '122'
when c.validator_to = 'cosmosvaloper125umsz3fws7gepn5ccsh0sv4gre9r6a3tccz4r' then '123'
when c.validator_to = 'cosmosvaloper14qazscc80zgzx3m0m0aa30ths0p9hg8vdglqrc' then '124'
when c.validator_to = 'cosmosvaloper1et77usu8q2hargvyusl4qzryev8x8t9wwqkxfs' then '125'
when c.validator_to = 'cosmosvaloper1485u80fdxjan4sd3esrvyw6cyurpvddvzuh48y' then '126'
when c.validator_to = 'cosmosvaloper1yw5s259jkcg0jzmh7sce29uk0lqqw2ump7578p' then '127'
when c.validator_to = 'cosmosvaloper1lkujuk2004p3w42tgvuvqnsdmsq8u6jqkwf9wj' then '128'
when c.validator_to = 'cosmosvaloper140e7u946a2nqqkvcnjpjm83d0ynsqem8dnp684' then '129'
when c.validator_to = 'cosmosvaloper13x77yexvf6qexfjg9czp6jhpv7vpjdwwkyhe4p' then '130'
when c.validator_to = 'cosmosvaloper1jxv0u20scum4trha72c7ltfgfqef6nsch7q6cu' then '131'
when c.validator_to = 'cosmosvaloper1qs8tnw2t8l6amtzvdemnnsq9dzk0ag0z52uzay' then '132'
when c.validator_to = 'cosmosvaloper1z66j0z75a9flwnez7sa8jxx46cqu4rfhd9q82w' then '133'
when c.validator_to = 'cosmosvaloper1648ynlpdw7fqa2axt0w2yp3fk542junl7rsvq6' then '134'
when c.validator_to = 'cosmosvaloper1j0vaeh27t4rll7zhmarwcuq8xtrmvqhudrgcky' then '135'
when c.validator_to = 'cosmosvaloper1v69lzl909kje64k8vae24uytpxcnpxgullz2dx' then '136'
when c.validator_to = 'cosmosvaloper103agss48504gkk3la5xcg5kxplaf6ttnuv234h' then '137'
when c.validator_to = 'cosmosvaloper1sdz4rc95vnzh2f54sacec50vjxnmwdakfym4vh' then '138'
when c.validator_to = 'cosmosvaloper12lfqufkk2h3w2ycp50czme6nj3ln5tdv7nj3hx' then '139'
when c.validator_to = 'cosmosvaloper1crqm3598z6qmyn2kkcl9dz7uqs4qdqnr6s8jdn' then '140'
when c.validator_to = 'cosmosvaloper1ukpah0340rx7k3x2njnavwyjv6pfpvn632df9q' then '141'
when c.validator_to = 'cosmosvaloper1ualhu3fjgg77g485gmyswkq3w0dp7gys6qzwrv' then '142'
when c.validator_to = 'cosmosvaloper13ql36flc4cdjhx08hke5vpr4dyv03aafnmvtnc' then '143'
when c.validator_to = 'cosmosvaloper1urxrvt5dmkqpe50gwrerjly2z6nvk9exjz2j3h' then '144'
when c.validator_to = 'cosmosvaloper1ff0dw8kawsnxkrgj7p65kvw7jxxakyf8n583gx' then '145'
when c.validator_to = 'cosmosvaloper1v78emy9d2xe3tj974l7tmn2whca2nh9zp7s0u9' then '146'
when c.validator_to = 'cosmosvaloper1kyfce0nvluyhgfsdzz8hwrsf5336gsc95pyy4u' then '147'
when c.validator_to = 'cosmosvaloper1ed5a27kfyu0yljmna00vtr8mgzp6rwh9zn77zz' then '148'
when c.validator_to = 'cosmosvaloper1usvshtypjw57edkwxq3tagme665398f0hf4wuc' then '149'
when c.validator_to = 'cosmosvaloper1ha8d55747h8hsaluvz8ld88n24nfaw68rx4x92' then '150'
when c.validator_to = 'cosmosvaloper1wlpz5hau2ezu0gmuxav63m53d8s77az9wfzlt6' then '151'
when c.validator_to = 'cosmosvaloper1zc0z44e42qhzltqc8qpj5qrzn836d3lftnqmgw' then '152'
when c.validator_to = 'cosmosvaloper1rj6324uq904z5zr96zg6ew9qjyau9u6h5nflg6' then '153'
when c.validator_to = 'cosmosvaloper1yh089p0cre4nhpdqw35uzde5amg3qzexkeggdn' then '154'
when c.validator_to = 'cosmosvaloper1a4qlael79p76my9pml6thwhnnzsxyy4ajrvd9s' then '155'
when c.validator_to = 'cosmosvaloper14upntdx8lf0f49t987mj99zksxnluanvu6x4lu' then '156'
when c.validator_to = 'cosmosvaloper1x3mkgqpshvpq87d33ndsleu7gd7w47dl4ve0yy' then '157'
when c.validator_to = 'cosmosvaloper10f9wkd6vdspac05djyfwfx0uxcqxapnqhnkcg8' then '158'
when c.validator_to = 'cosmosvaloper1yfnaup5wa3vdzx3wx9auhvzl85saqj37tqxqnu' then '159'
when c.validator_to = 'cosmosvaloper1wdrypwex63geqswmcy5qynv4w3z3dyef2qmyna' then '160'
when c.validator_to = 'cosmosvaloper1de7qx00pz2j6gn9k88ntxxylelkazfk3g8fgh9' then '161'
when c.validator_to = 'cosmosvaloper1nxe3gnztx8wvayj260dp6yw7jg797m8up02h7z' then '162'
when c.validator_to = 'cosmosvaloper1u6ddcsjueax884l3tfrs66497c7g86skn7pa0u' then '163'
when c.validator_to = 'cosmosvaloper1ec3p6a75mqwkv33zt543n6cnxqwun37rr5xlqv' then '164'
when c.validator_to = 'cosmosvaloper1fun809ksxh87nzf88yashp9ynjz6xkscrtvzvw' then '165'
when c.validator_to = 'cosmosvaloper1gf3dm2mvqhymts6ksrstlyuu2m8pw6dhfp9md2' then '166'
when c.validator_to = 'cosmosvaloper15r4tc0m6hc7z8drq3dzlrtcs6rq2q9l2nvwher' then '167'
when c.validator_to = 'cosmosvaloper1nz3c4q40j8jyvg2hcljkwhe69872mnllf7v9xh' then '168'
when c.validator_to = 'cosmosvaloper106yp7zw35wftheyyv9f9pe69t8rteumjrx52jg' then '169'
when c.validator_to = 'cosmosvaloper1v0g7guekttkdmerz5z8hjj8u8j68c6p00zqgf5' then '170'
when c.validator_to = 'cosmosvaloper12w6tynmjzq4l8zdla3v4x0jt8lt4rcz5gk7zg2' then '171'
when c.validator_to = 'cosmosvaloper1d0aup392g3enru7eash83sedqclaxvp7fzh6gk' then '172'
when c.validator_to = 'cosmosvaloper1s05va5d09xlq3et8mapsesqh6r5lqy7mkhwshm' then '173'
when c.validator_to = 'cosmosvaloper1n3nll7yl3lcv932s2r7l6jzvkjtjk0qppp3rls' then '174'
else '200' end as to_validator_rank,
sum(d.amount) as amount_redelegated  from table_9 a 
left join table_10 b 
on a.tx_id = b.tx_id 
left join table_11 c 
on a.tx_id = c.tx_id
left join table_12 d
on a.tx_id = d.tx_id 
group by from_validator, to_validator, from_validator_rank, to_validator_rank

	  
	"""  
	 

TTL_MINUTES = 15
# return up to 100,000 results per GET request on the query id
PAGE_SIZE = 100000
# return results of page 1
PAGE_NUMBER = 1
 
def create_query_2():
	r = requests.post(
			'https://node-api.flipsidecrypto.com/queries', 
			data=json.dumps({
				"sql": SQL_QUERY_2,
				"ttlMinutes": TTL_MINUTES
			}),
			headers={"Accept": "application/json", "Content-Type": "application/json", "x-api-key": API_KEY},
	)
	if r.status_code != 200:
		raise Exception("Error creating query, got response: " + r.text + "with status code: " + str(r.status_code))
		
	return json.loads(r.text)    
	 

 

def get_query_results_2(token):
	r = requests.get(
			'https://node-api.flipsidecrypto.com/queries/{token}?pageNumber={page_number}&pageSize={page_size}'.format(
			  token=token,
			  page_number=PAGE_NUMBER,
			  page_size=PAGE_SIZE
			),
			headers={"Accept": "application/json", "Content-Type": "application/json", "x-api-key": API_KEY}
	)
	if r.status_code != 200:
		raise Exception("Error getting query results, got response: " + r.text + "with status code: " + str(r.status_code))
		
	data = json.loads(r.text)
	if data['status'] == 'running':
		time.sleep(10)
		return get_query_results_2(token)

	return data


query_2 = create_query_2()
token_2 = query_2.get('token')
data2 = get_query_results_2(token_2) 
df2 = pd.DataFrame(data2['results'], columns = ['FROM_VALIDATOR', 'TO_VALIDATOR','FROM_VALIDATOR_RANK','TO_VALIDATOR_RANK','AMOUNT_REDELEGATED'])


	  


 

list1 = ['cosmosvaloper1sjllsnramtg3ewxqwwrwjxfgc4n4ef9u2lcnj0','cosmosvaloper1c4k24jzduc365kywrsvf5ujz4ya6mwympnc4en','cosmosvaloper14lultfckehtszvzw4ehu0apvsr77afvyju5zzy','cosmosvaloper1v5y0tg0jllvxf5c3afml8s3awue0ymju89frut','cosmosvaloper196ax4vc0lwpxndu9dyhvca7jhxp70rmcvrj90c','cosmosvaloper18ruzecmqj9pv8ac0gvkgryuc7u004te9rh7w5s','cosmosvaloper14k4pzckkre6uxxyd2lnhnpp8sngys9m6hl6ml7','cosmosvaloper1tflk30mq5vgqjdly92kkhhq3raev2hnz6eete3','cosmosvaloper1qaa9zej9a0ge3ugpx3pxyx602lxh3ztqgfnp42','cosmosvaloper19lss6zgdh5vvcpjhfftdghrpsw7a4434elpwpu','cosmosvaloper1ey69r37gfxvxg62sh4r0ktpuc46pzjrm873ae8','cosmosvaloper1hjct6q7npsspsg3dgvzk3sdf89spmlpfdn6m9d','cosmosvaloper1clpqr4nrk4khgkxj78fcwwh6dl3uw4epsluffn','cosmosvaloper156gqf9837u7d4c4678yt3rl4ls9c5vuursrrzf','cosmosvaloper132juzk0gdmwuxvx4phug7m3ymyatxlh9734g4w','cosmosvaloper15urq2dtp9qce4fyc85m6upwm9xul3049e02707','cosmosvaloper1z8zjv3lntpwxua0rtpvgrcwl0nm0tltgpgs6l7','cosmosvaloper1vf44d85es37hwl9f4h9gv0e064m0lla60j9luj','cosmosvaloper16k579jk6yt2cwmqx9dz5xvq9fug2tekvlu9qdv','cosmosvaloper1zqgheeawp7cmqk27dgyctd80rd8ryhqs6la9wc','cosmosvaloper1g48268mu5vfp4wk7dk89r0wdrakm9p5xk0q50k','cosmosvaloper1lzhlnpahvznwfv4jmay2tgaha5kmz5qxerarrl','cosmosvaloper1gpx52r9h3zeul45amvcy2pysgvcwddxrgx6cnv','cosmosvaloper1qwl879nx9t6kef4supyazayf7vjhennyh568ys','cosmosvaloper1gdg6qqe5a3u483unqlqsnullja23g0xvqkxtk0','cosmosvaloper1n229vhepft6wnkt5tjpwmxdmcnfz55jv3vp77d','cosmosvaloper1ma02nlc7lchu7caufyrrqt4r6v2mpsj90y9wzd','cosmosvaloper1vvwtk805lxehwle9l4yudmq6mn0g32px9xtkhc','cosmosvaloper1eh5mwu044gd5ntkkc2xgfg8247mgc56fz4sdg3','cosmosvaloper1grgelyng2v6v3t8z87wu3sxgt9m5s03xfytvz7','cosmosvaloper1te8nxpc2myjfrhaty0dnzdhs5ahdh5agzuym9v','cosmosvaloper1rpgtz9pskr5geavkjz02caqmeep7cwwpv73axj','cosmosvaloper14kn0kk33szpwus9nh8n87fjel8djx0y070ymmj','cosmosvaloper1y0us8xvsvfvqkk9c6nt5cfyu5au5tww2ztve7q','cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p','cosmosvaloper130mdu9a0etmeuw52qfxk73pn0ga6gawkxsrlwf','cosmosvaloper16fnz0v4cnv5dpnj0p3gaft2q2kzx8z5hfrx6v5','cosmosvaloper1we6knm8qartmmh2r0qfpsz6pq0s7emv3e0meuw','cosmosvaloper1jst8q8flpn94u9uvkpae8mrkk3a5pjhxx529z2','cosmosvaloper10e4vsut6suau8tk9m6dnrm0slgd6npe3jx5xpv','cosmosvaloper1kgddca7qj96z0qcxr2c45z73cfl0c75p7f3s2e','cosmosvaloper1cc99d3xcukhedg4wcw53j7a9q68uza707vpfe7','cosmosvaloper19rmlxkqjt950fxl849l49x0me56u9tkd5n5j62','cosmosvaloper199mlc7fr6ll5t54w7tts7f4s0cvnqgc59nmuxf','cosmosvaloper1k2d9ed9vgfuk2m58a2d80q9u6qljkh4vfaqjfq','cosmosvaloper10wljxpl03053h9690apmyeakly3ylhejrucvtm','cosmosvaloper1uutuwrwt3z2a5z8z3uasml3rftlpmu25aga5c6','cosmosvaloper1ssm0d433seakyak8kcf93yefhknjleeds4y3em','cosmosvaloper1ehkfl7palwrh6w2hhr2yfrgrq8jetgucudztfe','cosmosvaloper19yy989ka5usws6gsd8vl94y7l6ssgdwsrnscjc','cosmosvaloper1hjadhj9nqzpye2vkmkz4thahhd0z8dh3udhq74','cosmosvaloper157v7tczs40axfgejp2m43kwuzqe0wsy0rv8puv','cosmosvaloper1gxju9ky3hwxvqqagrl3dxtl49kjpxq6wlqe6m5','cosmosvaloper1n3mhyp9fvcmuu8l0q8qvjy07x0rql8q46fe2xk','cosmosvaloper146kwpzhmleafmhtaxulfptyhnvwxzlvm87hwnm','cosmosvaloper1x8efhljzvs52u5xa6m7crcwes7v9u0nlwdgw30','cosmosvaloper14l0fp639yudfl46zauvv8rkzjgd4u0zk2aseys','cosmosvaloper13nvnv6q8d3yg7tjeahjzljkqu0y27s8y9e7as9','cosmosvaloper1dqp325was50l7ut2lnx6s8xhmtwj3wrtx06gzu','cosmosvaloper1lktjhnzkpkz3ehrg8psvmwhafg56kfss3q3t8m','cosmosvaloper1udpsgkgyutgsglauk9vk9rs03a3skc62gup9ny','cosmosvaloper10nzaaeh2kq28t3nqsh5m8kmyv90vx7ym5mpakx','cosmosvaloper1sd4tl9aljmmezzudugs7zlaya7pg2895ws8tfs','cosmosvaloper124maqmcqv8tquy764ktz7cu0gxnzfw54n3vww8','cosmosvaloper1uhnsxv6m83jj3328mhrql7yax3nge5svrv6t6c','cosmosvaloper1ptyzewnns2kn37ewtmv6ppsvhdnmeapvtfc9y5','cosmosvaloper157qezau9xnzypse3vu2vhs7r4ee83fdecew0fz','cosmosvaloper1ul2me6vukg2vac2p6ltxmqlaa7jywdgt8q76ag','cosmosvaloper17mggn4znyeyg25wd7498qxl7r2jhgue8u4qjcq','cosmosvaloper1q6d3d089hg59x6gcx92uumx70s5y5wadklue8s','cosmosvaloper1sxx9mszve0gaedz5ld7qdkjkfv8z992ax69k08','cosmosvaloper1lcwxu50rvvgf9v6jy6q5mrzyhlszwtjxhtscmp','cosmosvaloper1dt93l3qgmhhlp97srjyqyendrgu9nx0suxtwe8','cosmosvaloper1ej2es5fjztqjcd4pwa0zyvaevtjd2y5wxxp9gd','cosmosvaloper1gjtvly9lel6zskvwtvlg5vhwpu9c9waw7sxzwx','cosmosvaloper1r2dthxctqzhwg299e7aaeqwfkgcc9hg8k3yd7m','cosmosvaloper1pjmngrwcsatsuyy8m3qrunaun67sr9x7z5r2qs','cosmosvaloper10jzj3jjd3frna0ay08sh4zu4fpy957s49jkk7m','cosmosvaloper1m73mgwn3cm2e8x9a9axa0kw8nqz8a492ms63vn','cosmosvaloper1symf474wnypes2d3mecllqk6l26rwz8mfjqdus','cosmosvaloper1hdrlqvyjfy5sdrseecjrutyws9khtxxaux62l7','cosmosvaloper17h2x3j7u44qkrq0sk8ul0r2qr440rwgjkfg0gh','cosmosvaloper1gf4wlkutql95j7wwsxz490s6fahlvk2s9xpwax','cosmosvaloper1cgh5ksjwy2sd407lyre4l3uj2fdrqhpkzp06e6','cosmosvaloper13sduv92y3xdhy3rpmhakrc3v7t37e7ps9l0kpv','cosmosvaloper1gp957czryfgyvxwn3tfnyy2f0t9g2p4pqeemx8','cosmosvaloper1083svrca4t350mphfv9x45wq9asrs60cdmrflj','cosmosvaloper1nuhls0wyf8slhmuasha5pz0u89jrf9nnugq8ak','cosmosvaloper1x8rr4hcf54nz6hfckyy2n05sxss54h8wz9puzg','cosmosvaloper1thl5syhmscgnj7whdyrydw3w6vy80044hjpnxh','cosmosvaloper1keltez56g3zm9w8wr8gcmmulze48g2q3usuw8c','cosmosvaloper140l6y2gp3gxvay6qtn70re7z2s0gn57zfd832j','cosmosvaloper1ddle9tczl87gsvmeva3c48nenyng4n56nghmjk','cosmosvaloper1rwh0cxa72d3yle3r4l8gd7vyphrmjy2kpe4x72','cosmosvaloper19ecn7ljwp6el2pc5lldyauwv05ufwut9mm38r5','cosmosvaloper1fhr7e04ct0zslmkzqt9smakg3sxrdve6ulclj2','cosmosvaloper1jlr62guqwrwkdt4m3y00zh2rrsamhjf9num5xr','cosmosvaloper122j3zmqdl6d2g64qmjuqzj65gfejsvjp07yljn','cosmosvaloper1xym2qygmr9vanpa0m7ndk3n0qxgey3ffzcyd5c','cosmosvaloper1e4vye322gkjx8n85jgcclnc7nvdvu82axnr5ll','cosmosvaloper13maqgtlklmereflvg3lq3e8zrp0jsqhr8ef3kk','cosmosvaloper1kn3wugetjuy4zetlq6wadchfhvu3x740ae6z6x','cosmosvaloper1svwt2mr4x2mx0hcmty0mxsa4rmlfau4lwx2l69','cosmosvaloper1wrx0x9m9ykdhw9sg04v7uljme53wuj03aa5d4f','cosmosvaloper16yupepagywvlk7uhpfchtwa0stu5f8cyhh54f2','cosmosvaloper18extdhzzl5c8tr6453e5hzaj3exrdlea90fj3y','cosmosvaloper1e859xaue4k2jzqw20cv6l7p3tmc378pc3k8g2u','cosmosvaloper1rcp29q3hpd246n6qak7jluqep4v006cdsc2kkl','cosmosvaloper1vygmh344ldv9qefss9ek7ggsnxparljlmj56q5','cosmosvaloper16s96n9k9zztdgjy8q4qcxp4hn7ww98qkrka4zk','cosmosvaloper1wqy2s6nwnxj57l0l5rdjxxr646p3al6y70435m','cosmosvaloper1xnrth5rku3z3msm9prxe3l0p2yec3d9mzxz9ka','cosmosvaloper102ruvpv2srmunfffxavttxnhezln6fnc54at8c','cosmosvaloper1fsg635n5vgc7jazz9sx5725wnc3xqgr7awxaag','cosmosvaloper1xwazl8ftks4gn00y5x3c47auquc62ssuqlj02r','cosmosvaloper1e0plfg475phrsvrlzw8gwppeva0zk5yg9fgg8c','cosmosvaloper10unx6s0cdqntvrumd5hs07rgd5ytcztqh8etw6','cosmosvaloper1fqzqejwkk898fcslw4z4eeqjzesynvrdfr5hte','cosmosvaloper142w8q2l0gxsfna72gq8t7e4ee4ul37e9htgtxx','cosmosvaloper1jmykcq8gylmy5tgqtel4xj4q62fdt49sl584xd','cosmosvaloper16qme5yxucnaj6snx35nmwze0wyxr8wfgqxsqfw','cosmosvaloper1aewyh4gtvayx6v7w592jdfylawk4rsu9tfvfgm','cosmosvaloper125umsz3fws7gepn5ccsh0sv4gre9r6a3tccz4r','cosmosvaloper14qazscc80zgzx3m0m0aa30ths0p9hg8vdglqrc','cosmosvaloper1et77usu8q2hargvyusl4qzryev8x8t9wwqkxfs','cosmosvaloper1485u80fdxjan4sd3esrvyw6cyurpvddvzuh48y','cosmosvaloper1yw5s259jkcg0jzmh7sce29uk0lqqw2ump7578p','cosmosvaloper1lkujuk2004p3w42tgvuvqnsdmsq8u6jqkwf9wj','cosmosvaloper140e7u946a2nqqkvcnjpjm83d0ynsqem8dnp684','cosmosvaloper13x77yexvf6qexfjg9czp6jhpv7vpjdwwkyhe4p','cosmosvaloper1jxv0u20scum4trha72c7ltfgfqef6nsch7q6cu','cosmosvaloper1qs8tnw2t8l6amtzvdemnnsq9dzk0ag0z52uzay','cosmosvaloper1z66j0z75a9flwnez7sa8jxx46cqu4rfhd9q82w','cosmosvaloper1648ynlpdw7fqa2axt0w2yp3fk542junl7rsvq6','cosmosvaloper1j0vaeh27t4rll7zhmarwcuq8xtrmvqhudrgcky','cosmosvaloper1v69lzl909kje64k8vae24uytpxcnpxgullz2dx','cosmosvaloper103agss48504gkk3la5xcg5kxplaf6ttnuv234h','cosmosvaloper1sdz4rc95vnzh2f54sacec50vjxnmwdakfym4vh','cosmosvaloper12lfqufkk2h3w2ycp50czme6nj3ln5tdv7nj3hx','cosmosvaloper1crqm3598z6qmyn2kkcl9dz7uqs4qdqnr6s8jdn','cosmosvaloper1ukpah0340rx7k3x2njnavwyjv6pfpvn632df9q','cosmosvaloper1ualhu3fjgg77g485gmyswkq3w0dp7gys6qzwrv','cosmosvaloper13ql36flc4cdjhx08hke5vpr4dyv03aafnmvtnc','cosmosvaloper1urxrvt5dmkqpe50gwrerjly2z6nvk9exjz2j3h','cosmosvaloper1ff0dw8kawsnxkrgj7p65kvw7jxxakyf8n583gx','cosmosvaloper1v78emy9d2xe3tj974l7tmn2whca2nh9zp7s0u9','cosmosvaloper1kyfce0nvluyhgfsdzz8hwrsf5336gsc95pyy4u','cosmosvaloper1ed5a27kfyu0yljmna00vtr8mgzp6rwh9zn77zz','cosmosvaloper1usvshtypjw57edkwxq3tagme665398f0hf4wuc','cosmosvaloper1ha8d55747h8hsaluvz8ld88n24nfaw68rx4x92','cosmosvaloper1wlpz5hau2ezu0gmuxav63m53d8s77az9wfzlt6','cosmosvaloper1zc0z44e42qhzltqc8qpj5qrzn836d3lftnqmgw','cosmosvaloper1rj6324uq904z5zr96zg6ew9qjyau9u6h5nflg6','cosmosvaloper1yh089p0cre4nhpdqw35uzde5amg3qzexkeggdn','cosmosvaloper1a4qlael79p76my9pml6thwhnnzsxyy4ajrvd9s','cosmosvaloper14upntdx8lf0f49t987mj99zksxnluanvu6x4lu','cosmosvaloper1x3mkgqpshvpq87d33ndsleu7gd7w47dl4ve0yy','cosmosvaloper10f9wkd6vdspac05djyfwfx0uxcqxapnqhnkcg8','cosmosvaloper1yfnaup5wa3vdzx3wx9auhvzl85saqj37tqxqnu','cosmosvaloper1wdrypwex63geqswmcy5qynv4w3z3dyef2qmyna','cosmosvaloper1de7qx00pz2j6gn9k88ntxxylelkazfk3g8fgh9','cosmosvaloper1nxe3gnztx8wvayj260dp6yw7jg797m8up02h7z','cosmosvaloper1u6ddcsjueax884l3tfrs66497c7g86skn7pa0u','cosmosvaloper1ec3p6a75mqwkv33zt543n6cnxqwun37rr5xlqv','cosmosvaloper1fun809ksxh87nzf88yashp9ynjz6xkscrtvzvw','cosmosvaloper1gf3dm2mvqhymts6ksrstlyuu2m8pw6dhfp9md2','cosmosvaloper15r4tc0m6hc7z8drq3dzlrtcs6rq2q9l2nvwher','cosmosvaloper1nz3c4q40j8jyvg2hcljkwhe69872mnllf7v9xh','cosmosvaloper106yp7zw35wftheyyv9f9pe69t8rteumjrx52jg','cosmosvaloper1v0g7guekttkdmerz5z8hjj8u8j68c6p00zqgf5','cosmosvaloper12w6tynmjzq4l8zdla3v4x0jt8lt4rcz5gk7zg2','cosmosvaloper1d0aup392g3enru7eash83sedqclaxvp7fzh6gk','cosmosvaloper1s05va5d09xlq3et8mapsesqh6r5lqy7mkhwshm','cosmosvaloper1n3nll7yl3lcv932s2r7l6jzvkjtjk0qppp3rls','other']
list2 = ['Stake fish ','Coinbase Custody','DokiaCapital','Zero Knowledge Validator (ZKV)','SG-1','Binance node','Polychain','Everstake','Game','Paradigm','Sika','Figment','Cosmostation','Binance staking','P2P.org','Chorus One','Kraken','Multichain ventures','Informal systems','No fee to 2025','Provalidator','Citadel.one','StakeLab','Certus One','Zugerselfdelegation','Allnodes.com','Hashtower','Imperator.co','Boubounode','Inqlusion','CoinoneNode','Blockpower','Forbole','Swiss Staking','Staking Facilities','strangelove-ventures','DACM','Staked','Node Guardians','B-Harvest','ChainLayer','dForce','Post Road','ShapeShift DAO','Stakecito','Ledger','DelegaNetworks ','IRISnet-Bianjie','KalpaTech','OKEx Pool','Atomic Nodes','POSTHUMAN DVS','Vortex.live','0base.vc','KysenPool Sky','Upbit Staking','ATEAM','Latent Iron','Nocturnal Labs','Umbrella ','AUDIT.one','Blockdaemon','InfStones','Simply Staking','S16 Research Ventures','WeStaking','KuCoin','HyperblocksPro','01node','Ubik Capital 0%Fee','e-Money.com // validator.network','stakezone','天照☀','Frens ','EZStaking.io','0% Fee 🌻 Sunflower','Cypher Core','Onbloc Node','#decentralizehk - DHK dao','BlockHunters ','SmartNodes','FreshATOMS.com','Stakewolle.com | Auto-compound','HashQuark','nylira.net','polkachu.com','Notional','Golden Ratio Staking','cosmosgbt','RockawayX Infra','DeFi Wallet','Lavender.Five Nodes 🐝','Witval','pe4x72','WhisperNode','Stakin','StakeWithUs','COS_Validator','🐡grant.fish','Binary Holdings','ChainUp','Huobi','Twinstake-Validator','Just-Mining','Stakely.io','Smart Stake','Citizen Cosmos','in3s.com','PUPMØS','Oni ','Klub Staking','coinhall.org','Ztake.org','cros-nest','jabbey','Easy 2 Stake','GATA DAO','commercio.network','NEOPLY','Blocks United | blocksunited.com','KIRA Staking','Silk Nodes','Moonstake','CryptoCrew Validators ✅','Stargaze','AIR DROP STATION','CEX.IO','BitValidator','danku_zone w/ DAIC','blockscape','Ping','Castlenode','debo-validator','Any Labs','Chainflow','Terra Nodes','MANTRA DAO','Chill Validation','Fanfury | fury.fan | Stake to Win','Coinbase Cloud','IcyCRO ','stake.systems','TienThuatToan Capital','zoomerlabs','Compass','a41','StakeSeeker by BTCS','CROSSTECH','Made In Block','Lightning Capital','🤑 uGaenn ⛅','Virtual Hive','Don Cryptonium','High Stakes 🇨🇭','Multiplex','Republic Crypto','CrowdControl','Tavis Digital','Moonlet','Genesis Lab','Cosmic Validator | Auto-compound','Synclub','Sentinel','lunamint','Tessellated','Blockapsis','DragonStake','Interstellar Lounge','Bro_n_Bro','LUNC DAO','Huobi-1','Stir','Wetez','RoundTable21 by WildSage Labs','Other']
list3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174, 200]

df1 = pd.DataFrame()

df1['ADDRESS'] = list1

df1['LABEL'] = list2

df1['RANK'] = list3

randcolor = []
for i in range(1,len(df1['LABEL']) + 1):
	 
	randcolor.append("#{:06x}".format(random.randint(0, 0xFFFFFF))) 
		
df1['COLOR'] = randcolor


keys_list =  df1['RANK']
values_list = df1['LABEL']
zip_iterator = zip(keys_list, values_list) 
a_dictionary = dict(zip_iterator)



df3 = pd.DataFrame(a_dictionary.items(), columns = ['RANK','LABEL'], index = keys_list)
df3.index = df3.index
df3 = df3.sort_index()



df2['FROM_VALIDATOR_RANK'] = df2['FROM_VALIDATOR_RANK'].astype('int')
df2['TO_VALIDATOR_RANK'] = df2['TO_VALIDATOR_RANK'].astype('int')


df2 = df2[df2['FROM_VALIDATOR'] != 'Other']


tab1, tab2 = st.tabs(
        [
            "Sankey chart for validators",
            "Sankey chat for total votes" 
        ])
with tab1:

		
	validator_choice = st.selectbox("Choose a validator", options = df2['FROM_VALIDATOR'].unique() )

		
	df_filtered = df2[df2['FROM_VALIDATOR'] == validator_choice]
	df_filtered['Link color'] = 'rgba(127, 194, 65, 0.2)'
	df_filtered['FROM_VALIDATOR_RANK'] = df_filtered['FROM_VALIDATOR_RANK']-1
	df_filtered['TO_VALIDATOR_RANK'] = df_filtered['TO_VALIDATOR_RANK'] - 1

	link = dict(source = df_filtered['FROM_VALIDATOR_RANK'].values , target = df_filtered['TO_VALIDATOR_RANK'].values, value = df_filtered['AMOUNT_REDELEGATED'], color = df1['COLOR'])
	node = dict(label = df3['LABEL'].values, pad = 35, thickness = 10)

	 
		
		 
	data = go.Sankey(link = link, node = node)
	fig = go.Figure(data)
	fig.update_layout(
			hovermode = 'x', 
			font = dict(size = 20, color = 'white'), 
			paper_bgcolor= 'rgba(0,0,0,0)',
			width=1000, height=1300
	) 
		
	st.plotly_chart(fig, use_container_width=True) 


with tab2:
    
        
    
    SQL_QUERY_3 = """ with table_8 as (
    select distinct tx_id from cosmos.core.fact_msg_attributes
    where tx_succeeded = 'TRUE'
    and msg_type = 'message'
    and attribute_key = 'action'
    and attribute_value = '/cosmos.staking.v1beta1.MsgBeginRedelegate'
    and to_date(block_timestamp) between '2022-10-31' and current_date 
    ),
    
    table_9 as (select distinct tx_id, attribute_value as address from cosmos.core.fact_msg_attributes
    where tx_succeeded = 'TRUE'
    and msg_type = 'transfer'
    and attribute_key = 'sender'
    and msg_index = '2'
    and tx_id in (select * from table_8)),
    
    table_10 as (select distinct tx_id, attribute_value as validator_from from cosmos.core.fact_msg_attributes
    where tx_succeeded = 'TRUE'
    and msg_type = 'redelegate'
    and attribute_key = 'source_validator'
    and tx_id in (select * from table_8)),
    
      
    table_11 as (select distinct tx_id, attribute_value as validator_to from cosmos.core.fact_msg_attributes
    where tx_succeeded = 'TRUE'
    and msg_type = 'redelegate'
    and attribute_key = 'destination_validator'
    and tx_id in (select * from table_8)),
    
      table_12 as (select distinct tx_id, to_number(SUBSTRING(attribute_value,0,CHARINDEX('uatom',attribute_value)-1))/pow(10,6) as amount from cosmos.core.fact_msg_attributes
    where tx_succeeded = 'TRUE'
    and msg_type = 'redelegate'
    and attribute_key = 'amount'
    and tx_id in (select * from table_8)),
    
    sankey_data as (  
    select 
    case when b.validator_from = 'cosmosvaloper1sjllsnramtg3ewxqwwrwjxfgc4n4ef9u2lcnj0' then 'Stake fish '
    
      when b.validator_from = 'cosmosvaloper1c4k24jzduc365kywrsvf5ujz4ya6mwympnc4en' then 'Coinbase Custody'
     when b.validator_from = 'cosmosvaloper14lultfckehtszvzw4ehu0apvsr77afvyju5zzy' then 'DokiaCapital'
     when b.validator_from = 'cosmosvaloper1v5y0tg0jllvxf5c3afml8s3awue0ymju89frut' then 'Zero Knowledge Validator (ZKV)'
     when b.validator_from = 'cosmosvaloper196ax4vc0lwpxndu9dyhvca7jhxp70rmcvrj90c' then 'SG-1'
     when b.validator_from = 'cosmosvaloper18ruzecmqj9pv8ac0gvkgryuc7u004te9rh7w5s' then 'Binance node'
     when b.validator_from = 'cosmosvaloper14k4pzckkre6uxxyd2lnhnpp8sngys9m6hl6ml7' then 'Polychain'
     when b.validator_from = 'cosmosvaloper1tflk30mq5vgqjdly92kkhhq3raev2hnz6eete3' then 'Everstake'
     when b.validator_from = 'cosmosvaloper1qaa9zej9a0ge3ugpx3pxyx602lxh3ztqgfnp42' then 'Game'
     when b.validator_from = 'cosmosvaloper19lss6zgdh5vvcpjhfftdghrpsw7a4434elpwpu' then 'Paradigm'
     when b.validator_from = 'cosmosvaloper1ey69r37gfxvxg62sh4r0ktpuc46pzjrm873ae8' then 'Sika'
     when b.validator_from = 'cosmosvaloper1hjct6q7npsspsg3dgvzk3sdf89spmlpfdn6m9d' then 'Figment'
     when b.validator_from = 'cosmosvaloper1clpqr4nrk4khgkxj78fcwwh6dl3uw4epsluffn' then 'Cosmostation'
     when b.validator_from = 'cosmosvaloper156gqf9837u7d4c4678yt3rl4ls9c5vuursrrzf' then 'Binance staking'
     when b.validator_from = 'cosmosvaloper132juzk0gdmwuxvx4phug7m3ymyatxlh9734g4w' then 'P2P.org'
     when b.validator_from = 'cosmosvaloper15urq2dtp9qce4fyc85m6upwm9xul3049e02707' then 'Chorus One'
     when b.validator_from = 'cosmosvaloper1z8zjv3lntpwxua0rtpvgrcwl0nm0tltgpgs6l7' then 'Kraken'
     when b.validator_from = 'cosmosvaloper1vf44d85es37hwl9f4h9gv0e064m0lla60j9luj' then 'Multichain ventures'
     when b.validator_from = 'cosmosvaloper16k579jk6yt2cwmqx9dz5xvq9fug2tekvlu9qdv' then 'Informal systems'
     when b.validator_from = 'cosmosvaloper1zqgheeawp7cmqk27dgyctd80rd8ryhqs6la9wc' then 'No fee to 2025'
     when b.validator_from = 'cosmosvaloper1g48268mu5vfp4wk7dk89r0wdrakm9p5xk0q50k' then 'Provalidator'
     when b.validator_from = 'cosmosvaloper1lzhlnpahvznwfv4jmay2tgaha5kmz5qxerarrl' then 'Citadel.one'
     when b.validator_from = 'cosmosvaloper1gpx52r9h3zeul45amvcy2pysgvcwddxrgx6cnv' then 'StakeLab'
     when b.validator_from = 'cosmosvaloper1qwl879nx9t6kef4supyazayf7vjhennyh568ys' then 'Certus One'
     when b.validator_from = 'cosmosvaloper1gdg6qqe5a3u483unqlqsnullja23g0xvqkxtk0' then 'Zugerselfdelegation'
     when b.validator_from = 'cosmosvaloper1n229vhepft6wnkt5tjpwmxdmcnfz55jv3vp77d' then 'Allnodes.com'
     when b.validator_from = 'cosmosvaloper1ma02nlc7lchu7caufyrrqt4r6v2mpsj90y9wzd' then 'Hashtower'
     when b.validator_from = 'cosmosvaloper1vvwtk805lxehwle9l4yudmq6mn0g32px9xtkhc' then 'Imperator.co'
     when b.validator_from = 'cosmosvaloper1eh5mwu044gd5ntkkc2xgfg8247mgc56fz4sdg3' then 'Boubounode'
     when b.validator_from = 'cosmosvaloper1grgelyng2v6v3t8z87wu3sxgt9m5s03xfytvz7' then 'Inqlusion'
     when b.validator_from = 'cosmosvaloper1te8nxpc2myjfrhaty0dnzdhs5ahdh5agzuym9v' then 'CoinoneNode'
     when b.validator_from = 'cosmosvaloper1rpgtz9pskr5geavkjz02caqmeep7cwwpv73axj' then 'Blockpower'
     when b.validator_from = 'cosmosvaloper14kn0kk33szpwus9nh8n87fjel8djx0y070ymmj' then 'Forbole'
     when b.validator_from = 'cosmosvaloper1y0us8xvsvfvqkk9c6nt5cfyu5au5tww2ztve7q' then 'Swiss Staking'
     when b.validator_from = 'cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p' then 'Staking Facilities'
     when b.validator_from = 'cosmosvaloper130mdu9a0etmeuw52qfxk73pn0ga6gawkxsrlwf' then 'strangelove-ventures'
     when b.validator_from = 'cosmosvaloper16fnz0v4cnv5dpnj0p3gaft2q2kzx8z5hfrx6v5' then 'DACM'
     when b.validator_from = 'cosmosvaloper1we6knm8qartmmh2r0qfpsz6pq0s7emv3e0meuw' then 'Staked'
     when b.validator_from = 'cosmosvaloper1jst8q8flpn94u9uvkpae8mrkk3a5pjhxx529z2' then 'Node Guardians'
     when b.validator_from = 'cosmosvaloper10e4vsut6suau8tk9m6dnrm0slgd6npe3jx5xpv' then 'B-Harvest'
     when b.validator_from = 'cosmosvaloper1kgddca7qj96z0qcxr2c45z73cfl0c75p7f3s2e' then 'ChainLayer'
     when b.validator_from = 'cosmosvaloper1cc99d3xcukhedg4wcw53j7a9q68uza707vpfe7' then 'dForce'
     when b.validator_from = 'cosmosvaloper19rmlxkqjt950fxl849l49x0me56u9tkd5n5j62' then 'Post Road'
     when b.validator_from = 'cosmosvaloper199mlc7fr6ll5t54w7tts7f4s0cvnqgc59nmuxf' then 'ShapeShift DAO'
     when b.validator_from = 'cosmosvaloper1k2d9ed9vgfuk2m58a2d80q9u6qljkh4vfaqjfq' then 'Stakecito'
     when b.validator_from = 'cosmosvaloper10wljxpl03053h9690apmyeakly3ylhejrucvtm' then 'Ledger'
     when b.validator_from = 'cosmosvaloper1uutuwrwt3z2a5z8z3uasml3rftlpmu25aga5c6' then 'DelegaNetworks '
     when b.validator_from = 'cosmosvaloper1ssm0d433seakyak8kcf93yefhknjleeds4y3em' then 'IRISnet-Bianjie'
     when b.validator_from = 'cosmosvaloper1ehkfl7palwrh6w2hhr2yfrgrq8jetgucudztfe' then 'KalpaTech'
     when b.validator_from = 'cosmosvaloper19yy989ka5usws6gsd8vl94y7l6ssgdwsrnscjc' then 'OKEx Pool'
     when b.validator_from = 'cosmosvaloper1hjadhj9nqzpye2vkmkz4thahhd0z8dh3udhq74' then 'Atomic Nodes'
     when b.validator_from = 'cosmosvaloper157v7tczs40axfgejp2m43kwuzqe0wsy0rv8puv' then 'POSTHUMAN DVS'
     when b.validator_from = 'cosmosvaloper1gxju9ky3hwxvqqagrl3dxtl49kjpxq6wlqe6m5' then 'Vortex.live'
     when b.validator_from = 'cosmosvaloper1n3mhyp9fvcmuu8l0q8qvjy07x0rql8q46fe2xk' then '0base.vc'
     when b.validator_from = 'cosmosvaloper146kwpzhmleafmhtaxulfptyhnvwxzlvm87hwnm' then 'KysenPool Sky'
     when b.validator_from = 'cosmosvaloper1x8efhljzvs52u5xa6m7crcwes7v9u0nlwdgw30' then 'Upbit Staking'
     when b.validator_from = 'cosmosvaloper14l0fp639yudfl46zauvv8rkzjgd4u0zk2aseys' then 'ATEAM'
     when b.validator_from = 'cosmosvaloper13nvnv6q8d3yg7tjeahjzljkqu0y27s8y9e7as9' then 'Latent Iron'
     when b.validator_from = 'cosmosvaloper1dqp325was50l7ut2lnx6s8xhmtwj3wrtx06gzu' then 'Nocturnal Labs'
     when b.validator_from = 'cosmosvaloper1lktjhnzkpkz3ehrg8psvmwhafg56kfss3q3t8m' then 'Umbrella '
     when b.validator_from = 'cosmosvaloper1udpsgkgyutgsglauk9vk9rs03a3skc62gup9ny' then 'AUDIT.one'
     when b.validator_from = 'cosmosvaloper10nzaaeh2kq28t3nqsh5m8kmyv90vx7ym5mpakx' then 'Blockdaemon'
     when b.validator_from = 'cosmosvaloper1sd4tl9aljmmezzudugs7zlaya7pg2895ws8tfs' then 'InfStones'
     when b.validator_from = 'cosmosvaloper124maqmcqv8tquy764ktz7cu0gxnzfw54n3vww8' then 'Simply Staking'
     when b.validator_from = 'cosmosvaloper1uhnsxv6m83jj3328mhrql7yax3nge5svrv6t6c' then 'S16 Research Ventures'
     when b.validator_from = 'cosmosvaloper1ptyzewnns2kn37ewtmv6ppsvhdnmeapvtfc9y5' then 'WeStaking'
     when b.validator_from = 'cosmosvaloper157qezau9xnzypse3vu2vhs7r4ee83fdecew0fz' then 'KuCoin'
     when b.validator_from = 'cosmosvaloper1ul2me6vukg2vac2p6ltxmqlaa7jywdgt8q76ag' then 'HyperblocksPro'
     when b.validator_from = 'cosmosvaloper17mggn4znyeyg25wd7498qxl7r2jhgue8u4qjcq' then '01node'
     when b.validator_from = 'cosmosvaloper1q6d3d089hg59x6gcx92uumx70s5y5wadklue8s' then 'Ubik Capital 0%Fee'
     when b.validator_from = 'cosmosvaloper1sxx9mszve0gaedz5ld7qdkjkfv8z992ax69k08' then 'e-Money.com // validator.network'
     when b.validator_from = 'cosmosvaloper1lcwxu50rvvgf9v6jy6q5mrzyhlszwtjxhtscmp' then 'stakezone'
     when b.validator_from = 'cosmosvaloper1dt93l3qgmhhlp97srjyqyendrgu9nx0suxtwe8' then '天照☀'
     when b.validator_from = 'cosmosvaloper1ej2es5fjztqjcd4pwa0zyvaevtjd2y5wxxp9gd' then 'Frens '
     when b.validator_from = 'cosmosvaloper1gjtvly9lel6zskvwtvlg5vhwpu9c9waw7sxzwx' then 'EZStaking.io'
     when b.validator_from = 'cosmosvaloper1r2dthxctqzhwg299e7aaeqwfkgcc9hg8k3yd7m' then '0% Fee 🌻 Sunflower'
     when b.validator_from = 'cosmosvaloper1pjmngrwcsatsuyy8m3qrunaun67sr9x7z5r2qs' then 'Cypher Core'
     when b.validator_from = 'cosmosvaloper10jzj3jjd3frna0ay08sh4zu4fpy957s49jkk7m' then 'Onbloc Node'
     when b.validator_from = 'cosmosvaloper1m73mgwn3cm2e8x9a9axa0kw8nqz8a492ms63vn' then '#decentralizehk - DHK dao'
     when b.validator_from = 'cosmosvaloper1symf474wnypes2d3mecllqk6l26rwz8mfjqdus' then 'BlockHunters '
     when b.validator_from = 'cosmosvaloper1hdrlqvyjfy5sdrseecjrutyws9khtxxaux62l7' then 'SmartNodes'
     when b.validator_from = 'cosmosvaloper17h2x3j7u44qkrq0sk8ul0r2qr440rwgjkfg0gh' then 'FreshATOMS.com'
     when b.validator_from = 'cosmosvaloper1gf4wlkutql95j7wwsxz490s6fahlvk2s9xpwax' then 'Stakewolle.com | Auto-compound'
     when b.validator_from = 'cosmosvaloper1cgh5ksjwy2sd407lyre4l3uj2fdrqhpkzp06e6' then 'HashQuark'
     when b.validator_from = 'cosmosvaloper13sduv92y3xdhy3rpmhakrc3v7t37e7ps9l0kpv' then 'nylira.net'
     when b.validator_from = 'cosmosvaloper1gp957czryfgyvxwn3tfnyy2f0t9g2p4pqeemx8' then 'polkachu.com'
     when b.validator_from = 'cosmosvaloper1083svrca4t350mphfv9x45wq9asrs60cdmrflj' then 'Notional'
     when b.validator_from = 'cosmosvaloper1nuhls0wyf8slhmuasha5pz0u89jrf9nnugq8ak' then 'Golden Ratio Staking'
     when b.validator_from = 'cosmosvaloper1x8rr4hcf54nz6hfckyy2n05sxss54h8wz9puzg' then 'cosmosgbt'
     when b.validator_from = 'cosmosvaloper1thl5syhmscgnj7whdyrydw3w6vy80044hjpnxh' then 'RockawayX Infra'
     when b.validator_from = 'cosmosvaloper1keltez56g3zm9w8wr8gcmmulze48g2q3usuw8c' then 'DeFi Wallet'
     when b.validator_from = 'cosmosvaloper140l6y2gp3gxvay6qtn70re7z2s0gn57zfd832j' then 'Lavender.Five Nodes 🐝'
     when b.validator_from = 'cosmosvaloper1ddle9tczl87gsvmeva3c48nenyng4n56nghmjk' then 'Witval'
     when b.validator_from = 'cosmosvaloper1rwh0cxa72d3yle3r4l8gd7vyphrmjy2kpe4x72' then 'pe4x72'
     when b.validator_from = 'cosmosvaloper19ecn7ljwp6el2pc5lldyauwv05ufwut9mm38r5' then 'WhisperNode'
     when b.validator_from = 'cosmosvaloper1fhr7e04ct0zslmkzqt9smakg3sxrdve6ulclj2' then 'Stakin'
     when b.validator_from = 'cosmosvaloper1jlr62guqwrwkdt4m3y00zh2rrsamhjf9num5xr' then 'StakeWithUs'
     when b.validator_from = 'cosmosvaloper122j3zmqdl6d2g64qmjuqzj65gfejsvjp07yljn' then 'COS_Validator'
     when b.validator_from = 'cosmosvaloper1xym2qygmr9vanpa0m7ndk3n0qxgey3ffzcyd5c' then '🐡grant.fish'
     when b.validator_from = 'cosmosvaloper1e4vye322gkjx8n85jgcclnc7nvdvu82axnr5ll' then 'Binary Holdings'
     when b.validator_from = 'cosmosvaloper13maqgtlklmereflvg3lq3e8zrp0jsqhr8ef3kk' then 'ChainUp'
     when b.validator_from = 'cosmosvaloper1kn3wugetjuy4zetlq6wadchfhvu3x740ae6z6x' then 'Huobi'
     when b.validator_from = 'cosmosvaloper1svwt2mr4x2mx0hcmty0mxsa4rmlfau4lwx2l69' then 'Twinstake-Validator'
     when b.validator_from = 'cosmosvaloper1wrx0x9m9ykdhw9sg04v7uljme53wuj03aa5d4f' then 'Just-Mining'
     when b.validator_from = 'cosmosvaloper16yupepagywvlk7uhpfchtwa0stu5f8cyhh54f2' then 'Stakely.io'
     when b.validator_from = 'cosmosvaloper18extdhzzl5c8tr6453e5hzaj3exrdlea90fj3y' then 'Smart Stake'
     when b.validator_from = 'cosmosvaloper1e859xaue4k2jzqw20cv6l7p3tmc378pc3k8g2u' then 'Citizen Cosmos'
     when b.validator_from = 'cosmosvaloper1rcp29q3hpd246n6qak7jluqep4v006cdsc2kkl' then 'in3s.com'
     when b.validator_from = 'cosmosvaloper1vygmh344ldv9qefss9ek7ggsnxparljlmj56q5' then 'PUPMØS'
     when b.validator_from = 'cosmosvaloper16s96n9k9zztdgjy8q4qcxp4hn7ww98qkrka4zk' then 'Oni '
     when b.validator_from = 'cosmosvaloper1wqy2s6nwnxj57l0l5rdjxxr646p3al6y70435m' then 'Klub Staking'
     when b.validator_from = 'cosmosvaloper1xnrth5rku3z3msm9prxe3l0p2yec3d9mzxz9ka' then 'coinhall.org'
     when b.validator_from = 'cosmosvaloper102ruvpv2srmunfffxavttxnhezln6fnc54at8c' then 'Ztake.org'
     when b.validator_from = 'cosmosvaloper1fsg635n5vgc7jazz9sx5725wnc3xqgr7awxaag' then 'cros-nest'
     when b.validator_from = 'cosmosvaloper1xwazl8ftks4gn00y5x3c47auquc62ssuqlj02r' then 'jabbey'
     when b.validator_from = 'cosmosvaloper1e0plfg475phrsvrlzw8gwppeva0zk5yg9fgg8c' then 'Easy 2 Stake'
     when b.validator_from = 'cosmosvaloper10unx6s0cdqntvrumd5hs07rgd5ytcztqh8etw6' then 'GATA DAO'
     when b.validator_from = 'cosmosvaloper1fqzqejwkk898fcslw4z4eeqjzesynvrdfr5hte' then 'commercio.network'
     when b.validator_from = 'cosmosvaloper142w8q2l0gxsfna72gq8t7e4ee4ul37e9htgtxx' then 'NEOPLY'
     when b.validator_from = 'cosmosvaloper1jmykcq8gylmy5tgqtel4xj4q62fdt49sl584xd' then 'Blocks United | blocksunited.com'
     when b.validator_from = 'cosmosvaloper16qme5yxucnaj6snx35nmwze0wyxr8wfgqxsqfw' then 'KIRA Staking'
     when b.validator_from = 'cosmosvaloper1aewyh4gtvayx6v7w592jdfylawk4rsu9tfvfgm' then 'Silk Nodes'
     when b.validator_from = 'cosmosvaloper125umsz3fws7gepn5ccsh0sv4gre9r6a3tccz4r' then 'Moonstake'
     when b.validator_from = 'cosmosvaloper14qazscc80zgzx3m0m0aa30ths0p9hg8vdglqrc' then 'CryptoCrew Validators ✅'
     when b.validator_from = 'cosmosvaloper1et77usu8q2hargvyusl4qzryev8x8t9wwqkxfs' then 'Stargaze'
     when b.validator_from = 'cosmosvaloper1485u80fdxjan4sd3esrvyw6cyurpvddvzuh48y' then 'AIR DROP STATION'
     when b.validator_from = 'cosmosvaloper1yw5s259jkcg0jzmh7sce29uk0lqqw2ump7578p' then 'CEX.IO'
     when b.validator_from = 'cosmosvaloper1lkujuk2004p3w42tgvuvqnsdmsq8u6jqkwf9wj' then 'BitValidator'
     when b.validator_from = 'cosmosvaloper140e7u946a2nqqkvcnjpjm83d0ynsqem8dnp684' then 'danku_zone w/ DAIC'
     when b.validator_from = 'cosmosvaloper13x77yexvf6qexfjg9czp6jhpv7vpjdwwkyhe4p' then 'blockscape'
     when b.validator_from = 'cosmosvaloper1jxv0u20scum4trha72c7ltfgfqef6nsch7q6cu' then 'Ping'
     when b.validator_from = 'cosmosvaloper1qs8tnw2t8l6amtzvdemnnsq9dzk0ag0z52uzay' then 'Castlenode'
     when b.validator_from = 'cosmosvaloper1z66j0z75a9flwnez7sa8jxx46cqu4rfhd9q82w' then 'debo-validator'
     when b.validator_from = 'cosmosvaloper1648ynlpdw7fqa2axt0w2yp3fk542junl7rsvq6' then 'Any Labs'
     when b.validator_from = 'cosmosvaloper1j0vaeh27t4rll7zhmarwcuq8xtrmvqhudrgcky' then 'Chainflow'
     when b.validator_from = 'cosmosvaloper1v69lzl909kje64k8vae24uytpxcnpxgullz2dx' then 'Terra Nodes'
     when b.validator_from = 'cosmosvaloper103agss48504gkk3la5xcg5kxplaf6ttnuv234h' then 'MANTRA DAO'
     when b.validator_from = 'cosmosvaloper1sdz4rc95vnzh2f54sacec50vjxnmwdakfym4vh' then 'Chill Validation'
     when b.validator_from = 'cosmosvaloper12lfqufkk2h3w2ycp50czme6nj3ln5tdv7nj3hx' then 'Fanfury | fury.fan | Stake to Win'
     when b.validator_from = 'cosmosvaloper1crqm3598z6qmyn2kkcl9dz7uqs4qdqnr6s8jdn' then 'Coinbase Cloud'
     when b.validator_from = 'cosmosvaloper1ukpah0340rx7k3x2njnavwyjv6pfpvn632df9q' then 'IcyCRO '
     when b.validator_from = 'cosmosvaloper1ualhu3fjgg77g485gmyswkq3w0dp7gys6qzwrv' then 'stake.systems'
     when b.validator_from = 'cosmosvaloper13ql36flc4cdjhx08hke5vpr4dyv03aafnmvtnc' then 'TienThuatToan Capital'
     when b.validator_from = 'cosmosvaloper1urxrvt5dmkqpe50gwrerjly2z6nvk9exjz2j3h' then 'zoomerlabs'
     when b.validator_from = 'cosmosvaloper1ff0dw8kawsnxkrgj7p65kvw7jxxakyf8n583gx' then 'Compass'
     when b.validator_from = 'cosmosvaloper1v78emy9d2xe3tj974l7tmn2whca2nh9zp7s0u9' then 'a41'
     when b.validator_from = 'cosmosvaloper1kyfce0nvluyhgfsdzz8hwrsf5336gsc95pyy4u' then 'StakeSeeker by BTCS'
     when b.validator_from = 'cosmosvaloper1ed5a27kfyu0yljmna00vtr8mgzp6rwh9zn77zz' then 'CROSSTECH'
     when b.validator_from = 'cosmosvaloper1usvshtypjw57edkwxq3tagme665398f0hf4wuc' then 'Made In Block'
     when b.validator_from = 'cosmosvaloper1ha8d55747h8hsaluvz8ld88n24nfaw68rx4x92' then 'Lightning Capital'
     when b.validator_from = 'cosmosvaloper1wlpz5hau2ezu0gmuxav63m53d8s77az9wfzlt6' then '🤑 uGaenn ⛅'
     when b.validator_from = 'cosmosvaloper1zc0z44e42qhzltqc8qpj5qrzn836d3lftnqmgw' then 'Virtual Hive'
     when b.validator_from = 'cosmosvaloper1rj6324uq904z5zr96zg6ew9qjyau9u6h5nflg6' then 'Don Cryptonium'
     when b.validator_from = 'cosmosvaloper1yh089p0cre4nhpdqw35uzde5amg3qzexkeggdn' then 'High Stakes 🇨🇭'
     when b.validator_from = 'cosmosvaloper1a4qlael79p76my9pml6thwhnnzsxyy4ajrvd9s' then 'Multiplex'
     when b.validator_from = 'cosmosvaloper14upntdx8lf0f49t987mj99zksxnluanvu6x4lu' then 'Republic Crypto'
     when b.validator_from = 'cosmosvaloper1x3mkgqpshvpq87d33ndsleu7gd7w47dl4ve0yy' then 'CrowdControl'
     when b.validator_from = 'cosmosvaloper10f9wkd6vdspac05djyfwfx0uxcqxapnqhnkcg8' then 'Tavis Digital'
     when b.validator_from = 'cosmosvaloper1yfnaup5wa3vdzx3wx9auhvzl85saqj37tqxqnu' then 'Moonlet'
     when b.validator_from = 'cosmosvaloper1wdrypwex63geqswmcy5qynv4w3z3dyef2qmyna' then 'Genesis Lab'
     when b.validator_from = 'cosmosvaloper1de7qx00pz2j6gn9k88ntxxylelkazfk3g8fgh9' then 'Cosmic Validator | Auto-compound'
     when b.validator_from = 'cosmosvaloper1nxe3gnztx8wvayj260dp6yw7jg797m8up02h7z' then 'Synclub'
     when b.validator_from = 'cosmosvaloper1u6ddcsjueax884l3tfrs66497c7g86skn7pa0u' then 'Sentinel'
     when b.validator_from = 'cosmosvaloper1ec3p6a75mqwkv33zt543n6cnxqwun37rr5xlqv' then 'lunamint'
     when b.validator_from = 'cosmosvaloper1fun809ksxh87nzf88yashp9ynjz6xkscrtvzvw' then 'Tessellated'
     when b.validator_from = 'cosmosvaloper1gf3dm2mvqhymts6ksrstlyuu2m8pw6dhfp9md2' then 'Blockapsis'
     when b.validator_from = 'cosmosvaloper15r4tc0m6hc7z8drq3dzlrtcs6rq2q9l2nvwher' then 'DragonStake'
     when b.validator_from = 'cosmosvaloper1nz3c4q40j8jyvg2hcljkwhe69872mnllf7v9xh' then 'Interstellar Lounge'
     when b.validator_from = 'cosmosvaloper106yp7zw35wftheyyv9f9pe69t8rteumjrx52jg' then 'Bro_n_Bro'
     when b.validator_from = 'cosmosvaloper1v0g7guekttkdmerz5z8hjj8u8j68c6p00zqgf5' then 'LUNC DAO'
     when b.validator_from = 'cosmosvaloper12w6tynmjzq4l8zdla3v4x0jt8lt4rcz5gk7zg2' then 'Huobi-1'
     when b.validator_from = 'cosmosvaloper1d0aup392g3enru7eash83sedqclaxvp7fzh6gk' then 'Stir'
     when b.validator_from = 'cosmosvaloper1s05va5d09xlq3et8mapsesqh6r5lqy7mkhwshm' then 'Wetez'
     when b.validator_from = 'cosmosvaloper1n3nll7yl3lcv932s2r7l6jzvkjtjk0qppp3rls' then 'RoundTable21 by WildSage Labs'
      else 'Other' end as from_validator, 
    
     case when validator_to = 'cosmosvaloper1sjllsnramtg3ewxqwwrwjxfgc4n4ef9u2lcnj0' then 'Stake fish '
     when validator_to = 'cosmosvaloper1c4k24jzduc365kywrsvf5ujz4ya6mwympnc4en' then 'Coinbase Custody'
     when validator_to = 'cosmosvaloper14lultfckehtszvzw4ehu0apvsr77afvyju5zzy' then 'DokiaCapital'
     when validator_to = 'cosmosvaloper1v5y0tg0jllvxf5c3afml8s3awue0ymju89frut' then 'Zero Knowledge Validator (ZKV)'
     when validator_to = 'cosmosvaloper196ax4vc0lwpxndu9dyhvca7jhxp70rmcvrj90c' then 'SG-1'
     when validator_to = 'cosmosvaloper18ruzecmqj9pv8ac0gvkgryuc7u004te9rh7w5s' then 'Binance node'
     when validator_to = 'cosmosvaloper14k4pzckkre6uxxyd2lnhnpp8sngys9m6hl6ml7' then 'Polychain'
     when validator_to = 'cosmosvaloper1tflk30mq5vgqjdly92kkhhq3raev2hnz6eete3' then 'Everstake'
     when validator_to = 'cosmosvaloper1qaa9zej9a0ge3ugpx3pxyx602lxh3ztqgfnp42' then 'Game'
     when validator_to = 'cosmosvaloper19lss6zgdh5vvcpjhfftdghrpsw7a4434elpwpu' then 'Paradigm'
     when validator_to = 'cosmosvaloper1ey69r37gfxvxg62sh4r0ktpuc46pzjrm873ae8' then 'Sika'
     when validator_to = 'cosmosvaloper1hjct6q7npsspsg3dgvzk3sdf89spmlpfdn6m9d' then 'Figment'
     when validator_to = 'cosmosvaloper1clpqr4nrk4khgkxj78fcwwh6dl3uw4epsluffn' then 'Cosmostation'
     when validator_to = 'cosmosvaloper156gqf9837u7d4c4678yt3rl4ls9c5vuursrrzf' then 'Binance staking'
     when validator_to = 'cosmosvaloper132juzk0gdmwuxvx4phug7m3ymyatxlh9734g4w' then 'P2P.org'
     when validator_to = 'cosmosvaloper15urq2dtp9qce4fyc85m6upwm9xul3049e02707' then 'Chorus One'
     when validator_to = 'cosmosvaloper1z8zjv3lntpwxua0rtpvgrcwl0nm0tltgpgs6l7' then 'Kraken'
     when validator_to = 'cosmosvaloper1vf44d85es37hwl9f4h9gv0e064m0lla60j9luj' then 'Multichain ventures'
     when validator_to = 'cosmosvaloper16k579jk6yt2cwmqx9dz5xvq9fug2tekvlu9qdv' then 'Informal systems'
     when validator_to = 'cosmosvaloper1zqgheeawp7cmqk27dgyctd80rd8ryhqs6la9wc' then 'No fee to 2025'
     when validator_to = 'cosmosvaloper1g48268mu5vfp4wk7dk89r0wdrakm9p5xk0q50k' then 'Provalidator'
     when validator_to = 'cosmosvaloper1lzhlnpahvznwfv4jmay2tgaha5kmz5qxerarrl' then 'Citadel.one'
     when validator_to = 'cosmosvaloper1gpx52r9h3zeul45amvcy2pysgvcwddxrgx6cnv' then 'StakeLab'
     when validator_to = 'cosmosvaloper1qwl879nx9t6kef4supyazayf7vjhennyh568ys' then 'Certus One'
     when validator_to = 'cosmosvaloper1gdg6qqe5a3u483unqlqsnullja23g0xvqkxtk0' then 'Zugerselfdelegation'
     when validator_to = 'cosmosvaloper1n229vhepft6wnkt5tjpwmxdmcnfz55jv3vp77d' then 'Allnodes.com'
     when validator_to = 'cosmosvaloper1ma02nlc7lchu7caufyrrqt4r6v2mpsj90y9wzd' then 'Hashtower'
     when validator_to = 'cosmosvaloper1vvwtk805lxehwle9l4yudmq6mn0g32px9xtkhc' then 'Imperator.co'
     when validator_to = 'cosmosvaloper1eh5mwu044gd5ntkkc2xgfg8247mgc56fz4sdg3' then 'Boubounode'
     when validator_to = 'cosmosvaloper1grgelyng2v6v3t8z87wu3sxgt9m5s03xfytvz7' then 'Inqlusion'
     when validator_to = 'cosmosvaloper1te8nxpc2myjfrhaty0dnzdhs5ahdh5agzuym9v' then 'CoinoneNode'
     when validator_to = 'cosmosvaloper1rpgtz9pskr5geavkjz02caqmeep7cwwpv73axj' then 'Blockpower'
     when validator_to = 'cosmosvaloper14kn0kk33szpwus9nh8n87fjel8djx0y070ymmj' then 'Forbole'
     when validator_to = 'cosmosvaloper1y0us8xvsvfvqkk9c6nt5cfyu5au5tww2ztve7q' then 'Swiss Staking'
     when validator_to = 'cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p' then 'Staking Facilities'
     when validator_to = 'cosmosvaloper130mdu9a0etmeuw52qfxk73pn0ga6gawkxsrlwf' then 'strangelove-ventures'
     when validator_to = 'cosmosvaloper16fnz0v4cnv5dpnj0p3gaft2q2kzx8z5hfrx6v5' then 'DACM'
     when validator_to = 'cosmosvaloper1we6knm8qartmmh2r0qfpsz6pq0s7emv3e0meuw' then 'Staked'
     when validator_to = 'cosmosvaloper1jst8q8flpn94u9uvkpae8mrkk3a5pjhxx529z2' then 'Node Guardians'
     when validator_to = 'cosmosvaloper10e4vsut6suau8tk9m6dnrm0slgd6npe3jx5xpv' then 'B-Harvest'
     when validator_to = 'cosmosvaloper1kgddca7qj96z0qcxr2c45z73cfl0c75p7f3s2e' then 'ChainLayer'
     when validator_to = 'cosmosvaloper1cc99d3xcukhedg4wcw53j7a9q68uza707vpfe7' then 'dForce'
     when validator_to = 'cosmosvaloper19rmlxkqjt950fxl849l49x0me56u9tkd5n5j62' then 'Post Road'
     when validator_to = 'cosmosvaloper199mlc7fr6ll5t54w7tts7f4s0cvnqgc59nmuxf' then 'ShapeShift DAO'
     when validator_to = 'cosmosvaloper1k2d9ed9vgfuk2m58a2d80q9u6qljkh4vfaqjfq' then 'Stakecito'
     when validator_to = 'cosmosvaloper10wljxpl03053h9690apmyeakly3ylhejrucvtm' then 'Ledger'
     when validator_to = 'cosmosvaloper1uutuwrwt3z2a5z8z3uasml3rftlpmu25aga5c6' then 'DelegaNetworks '
     when validator_to = 'cosmosvaloper1ssm0d433seakyak8kcf93yefhknjleeds4y3em' then 'IRISnet-Bianjie'
     when validator_to = 'cosmosvaloper1ehkfl7palwrh6w2hhr2yfrgrq8jetgucudztfe' then 'KalpaTech'
     when validator_to = 'cosmosvaloper19yy989ka5usws6gsd8vl94y7l6ssgdwsrnscjc' then 'OKEx Pool'
     when validator_to = 'cosmosvaloper1hjadhj9nqzpye2vkmkz4thahhd0z8dh3udhq74' then 'Atomic Nodes'
     when validator_to = 'cosmosvaloper157v7tczs40axfgejp2m43kwuzqe0wsy0rv8puv' then 'POSTHUMAN DVS'
     when validator_to = 'cosmosvaloper1gxju9ky3hwxvqqagrl3dxtl49kjpxq6wlqe6m5' then 'Vortex.live'
     when validator_to = 'cosmosvaloper1n3mhyp9fvcmuu8l0q8qvjy07x0rql8q46fe2xk' then '0base.vc'
     when validator_to = 'cosmosvaloper146kwpzhmleafmhtaxulfptyhnvwxzlvm87hwnm' then 'KysenPool Sky'
     when validator_to = 'cosmosvaloper1x8efhljzvs52u5xa6m7crcwes7v9u0nlwdgw30' then 'Upbit Staking'
     when validator_to = 'cosmosvaloper14l0fp639yudfl46zauvv8rkzjgd4u0zk2aseys' then 'ATEAM'
     when validator_to = 'cosmosvaloper13nvnv6q8d3yg7tjeahjzljkqu0y27s8y9e7as9' then 'Latent Iron'
     when validator_to = 'cosmosvaloper1dqp325was50l7ut2lnx6s8xhmtwj3wrtx06gzu' then 'Nocturnal Labs'
     when validator_to = 'cosmosvaloper1lktjhnzkpkz3ehrg8psvmwhafg56kfss3q3t8m' then 'Umbrella '
     when validator_to = 'cosmosvaloper1udpsgkgyutgsglauk9vk9rs03a3skc62gup9ny' then 'AUDIT.one'
     when validator_to = 'cosmosvaloper10nzaaeh2kq28t3nqsh5m8kmyv90vx7ym5mpakx' then 'Blockdaemon'
     when validator_to = 'cosmosvaloper1sd4tl9aljmmezzudugs7zlaya7pg2895ws8tfs' then 'InfStones'
     when validator_to = 'cosmosvaloper124maqmcqv8tquy764ktz7cu0gxnzfw54n3vww8' then 'Simply Staking'
     when validator_to = 'cosmosvaloper1uhnsxv6m83jj3328mhrql7yax3nge5svrv6t6c' then 'S16 Research Ventures'
     when validator_to = 'cosmosvaloper1ptyzewnns2kn37ewtmv6ppsvhdnmeapvtfc9y5' then 'WeStaking'
     when validator_to = 'cosmosvaloper157qezau9xnzypse3vu2vhs7r4ee83fdecew0fz' then 'KuCoin'
     when validator_to = 'cosmosvaloper1ul2me6vukg2vac2p6ltxmqlaa7jywdgt8q76ag' then 'HyperblocksPro'
     when validator_to = 'cosmosvaloper17mggn4znyeyg25wd7498qxl7r2jhgue8u4qjcq' then '01node'
     when validator_to = 'cosmosvaloper1q6d3d089hg59x6gcx92uumx70s5y5wadklue8s' then 'Ubik Capital 0%Fee'
     when validator_to = 'cosmosvaloper1sxx9mszve0gaedz5ld7qdkjkfv8z992ax69k08' then 'e-Money.com // validator.network'
     when validator_to = 'cosmosvaloper1lcwxu50rvvgf9v6jy6q5mrzyhlszwtjxhtscmp' then 'stakezone'
     when validator_to = 'cosmosvaloper1dt93l3qgmhhlp97srjyqyendrgu9nx0suxtwe8' then '天照☀'
     when validator_to = 'cosmosvaloper1ej2es5fjztqjcd4pwa0zyvaevtjd2y5wxxp9gd' then 'Frens '
     when validator_to = 'cosmosvaloper1gjtvly9lel6zskvwtvlg5vhwpu9c9waw7sxzwx' then 'EZStaking.io'
     when validator_to = 'cosmosvaloper1r2dthxctqzhwg299e7aaeqwfkgcc9hg8k3yd7m' then '0% Fee 🌻 Sunflower'
     when validator_to = 'cosmosvaloper1pjmngrwcsatsuyy8m3qrunaun67sr9x7z5r2qs' then 'Cypher Core'
     when validator_to = 'cosmosvaloper10jzj3jjd3frna0ay08sh4zu4fpy957s49jkk7m' then 'Onbloc Node'
     when validator_to = 'cosmosvaloper1m73mgwn3cm2e8x9a9axa0kw8nqz8a492ms63vn' then '#decentralizehk - DHK dao'
     when validator_to = 'cosmosvaloper1symf474wnypes2d3mecllqk6l26rwz8mfjqdus' then 'BlockHunters '
     when validator_to = 'cosmosvaloper1hdrlqvyjfy5sdrseecjrutyws9khtxxaux62l7' then 'SmartNodes'
     when validator_to = 'cosmosvaloper17h2x3j7u44qkrq0sk8ul0r2qr440rwgjkfg0gh' then 'FreshATOMS.com'
     when validator_to = 'cosmosvaloper1gf4wlkutql95j7wwsxz490s6fahlvk2s9xpwax' then 'Stakewolle.com | Auto-compound'
     when validator_to = 'cosmosvaloper1cgh5ksjwy2sd407lyre4l3uj2fdrqhpkzp06e6' then 'HashQuark'
     when validator_to = 'cosmosvaloper13sduv92y3xdhy3rpmhakrc3v7t37e7ps9l0kpv' then 'nylira.net'
     when validator_to = 'cosmosvaloper1gp957czryfgyvxwn3tfnyy2f0t9g2p4pqeemx8' then 'polkachu.com'
     when validator_to = 'cosmosvaloper1083svrca4t350mphfv9x45wq9asrs60cdmrflj' then 'Notional'
     when validator_to = 'cosmosvaloper1nuhls0wyf8slhmuasha5pz0u89jrf9nnugq8ak' then 'Golden Ratio Staking'
     when validator_to = 'cosmosvaloper1x8rr4hcf54nz6hfckyy2n05sxss54h8wz9puzg' then 'cosmosgbt'
     when validator_to = 'cosmosvaloper1thl5syhmscgnj7whdyrydw3w6vy80044hjpnxh' then 'RockawayX Infra'
     when validator_to = 'cosmosvaloper1keltez56g3zm9w8wr8gcmmulze48g2q3usuw8c' then 'DeFi Wallet'
     when validator_to = 'cosmosvaloper140l6y2gp3gxvay6qtn70re7z2s0gn57zfd832j' then 'Lavender.Five Nodes 🐝'
     when validator_to = 'cosmosvaloper1ddle9tczl87gsvmeva3c48nenyng4n56nghmjk' then 'Witval'
     when validator_to = 'cosmosvaloper1rwh0cxa72d3yle3r4l8gd7vyphrmjy2kpe4x72' then 'pe4x72'
     when validator_to = 'cosmosvaloper19ecn7ljwp6el2pc5lldyauwv05ufwut9mm38r5' then 'WhisperNode'
     when validator_to = 'cosmosvaloper1fhr7e04ct0zslmkzqt9smakg3sxrdve6ulclj2' then 'Stakin'
     when validator_to = 'cosmosvaloper1jlr62guqwrwkdt4m3y00zh2rrsamhjf9num5xr' then 'StakeWithUs'
     when validator_to = 'cosmosvaloper122j3zmqdl6d2g64qmjuqzj65gfejsvjp07yljn' then 'COS_Validator'
     when validator_to = 'cosmosvaloper1xym2qygmr9vanpa0m7ndk3n0qxgey3ffzcyd5c' then '🐡grant.fish'
     when validator_to = 'cosmosvaloper1e4vye322gkjx8n85jgcclnc7nvdvu82axnr5ll' then 'Binary Holdings'
     when validator_to = 'cosmosvaloper13maqgtlklmereflvg3lq3e8zrp0jsqhr8ef3kk' then 'ChainUp'
     when validator_to = 'cosmosvaloper1kn3wugetjuy4zetlq6wadchfhvu3x740ae6z6x' then 'Huobi'
     when validator_to = 'cosmosvaloper1svwt2mr4x2mx0hcmty0mxsa4rmlfau4lwx2l69' then 'Twinstake-Validator'
     when validator_to = 'cosmosvaloper1wrx0x9m9ykdhw9sg04v7uljme53wuj03aa5d4f' then 'Just-Mining'
     when validator_to = 'cosmosvaloper16yupepagywvlk7uhpfchtwa0stu5f8cyhh54f2' then 'Stakely.io'
     when validator_to = 'cosmosvaloper18extdhzzl5c8tr6453e5hzaj3exrdlea90fj3y' then 'Smart Stake'
     when validator_to = 'cosmosvaloper1e859xaue4k2jzqw20cv6l7p3tmc378pc3k8g2u' then 'Citizen Cosmos'
     when validator_to = 'cosmosvaloper1rcp29q3hpd246n6qak7jluqep4v006cdsc2kkl' then 'in3s.com'
     when validator_to = 'cosmosvaloper1vygmh344ldv9qefss9ek7ggsnxparljlmj56q5' then 'PUPMØS'
     when validator_to = 'cosmosvaloper16s96n9k9zztdgjy8q4qcxp4hn7ww98qkrka4zk' then 'Oni '
     when validator_to = 'cosmosvaloper1wqy2s6nwnxj57l0l5rdjxxr646p3al6y70435m' then 'Klub Staking'
     when validator_to = 'cosmosvaloper1xnrth5rku3z3msm9prxe3l0p2yec3d9mzxz9ka' then 'coinhall.org'
     when validator_to = 'cosmosvaloper102ruvpv2srmunfffxavttxnhezln6fnc54at8c' then 'Ztake.org'
     when validator_to = 'cosmosvaloper1fsg635n5vgc7jazz9sx5725wnc3xqgr7awxaag' then 'cros-nest'
     when validator_to = 'cosmosvaloper1xwazl8ftks4gn00y5x3c47auquc62ssuqlj02r' then 'jabbey'
     when validator_to = 'cosmosvaloper1e0plfg475phrsvrlzw8gwppeva0zk5yg9fgg8c' then 'Easy 2 Stake'
     when validator_to = 'cosmosvaloper10unx6s0cdqntvrumd5hs07rgd5ytcztqh8etw6' then 'GATA DAO'
     when validator_to = 'cosmosvaloper1fqzqejwkk898fcslw4z4eeqjzesynvrdfr5hte' then 'commercio.network'
     when validator_to = 'cosmosvaloper142w8q2l0gxsfna72gq8t7e4ee4ul37e9htgtxx' then 'NEOPLY'
     when validator_to = 'cosmosvaloper1jmykcq8gylmy5tgqtel4xj4q62fdt49sl584xd' then 'Blocks United | blocksunited.com'
     when validator_to = 'cosmosvaloper16qme5yxucnaj6snx35nmwze0wyxr8wfgqxsqfw' then 'KIRA Staking'
     when validator_to = 'cosmosvaloper1aewyh4gtvayx6v7w592jdfylawk4rsu9tfvfgm' then 'Silk Nodes'
     when validator_to = 'cosmosvaloper125umsz3fws7gepn5ccsh0sv4gre9r6a3tccz4r' then 'Moonstake'
     when validator_to = 'cosmosvaloper14qazscc80zgzx3m0m0aa30ths0p9hg8vdglqrc' then 'CryptoCrew Validators ✅'
     when validator_to = 'cosmosvaloper1et77usu8q2hargvyusl4qzryev8x8t9wwqkxfs' then 'Stargaze'
     when validator_to = 'cosmosvaloper1485u80fdxjan4sd3esrvyw6cyurpvddvzuh48y' then 'AIR DROP STATION'
     when validator_to = 'cosmosvaloper1yw5s259jkcg0jzmh7sce29uk0lqqw2ump7578p' then 'CEX.IO'
     when validator_to = 'cosmosvaloper1lkujuk2004p3w42tgvuvqnsdmsq8u6jqkwf9wj' then 'BitValidator'
     when validator_to = 'cosmosvaloper140e7u946a2nqqkvcnjpjm83d0ynsqem8dnp684' then 'danku_zone w/ DAIC'
     when validator_to = 'cosmosvaloper13x77yexvf6qexfjg9czp6jhpv7vpjdwwkyhe4p' then 'blockscape'
     when validator_to = 'cosmosvaloper1jxv0u20scum4trha72c7ltfgfqef6nsch7q6cu' then 'Ping'
     when validator_to = 'cosmosvaloper1qs8tnw2t8l6amtzvdemnnsq9dzk0ag0z52uzay' then 'Castlenode'
     when validator_to = 'cosmosvaloper1z66j0z75a9flwnez7sa8jxx46cqu4rfhd9q82w' then 'debo-validator'
     when validator_to = 'cosmosvaloper1648ynlpdw7fqa2axt0w2yp3fk542junl7rsvq6' then 'Any Labs'
     when validator_to = 'cosmosvaloper1j0vaeh27t4rll7zhmarwcuq8xtrmvqhudrgcky' then 'Chainflow'
     when validator_to = 'cosmosvaloper1v69lzl909kje64k8vae24uytpxcnpxgullz2dx' then 'Terra Nodes'
     when validator_to = 'cosmosvaloper103agss48504gkk3la5xcg5kxplaf6ttnuv234h' then 'MANTRA DAO'
     when validator_to = 'cosmosvaloper1sdz4rc95vnzh2f54sacec50vjxnmwdakfym4vh' then 'Chill Validation'
     when validator_to = 'cosmosvaloper12lfqufkk2h3w2ycp50czme6nj3ln5tdv7nj3hx' then 'Fanfury | fury.fan | Stake to Win'
     when validator_to = 'cosmosvaloper1crqm3598z6qmyn2kkcl9dz7uqs4qdqnr6s8jdn' then 'Coinbase Cloud'
     when validator_to = 'cosmosvaloper1ukpah0340rx7k3x2njnavwyjv6pfpvn632df9q' then 'IcyCRO '
     when validator_to = 'cosmosvaloper1ualhu3fjgg77g485gmyswkq3w0dp7gys6qzwrv' then 'stake.systems'
     when validator_to = 'cosmosvaloper13ql36flc4cdjhx08hke5vpr4dyv03aafnmvtnc' then 'TienThuatToan Capital'
     when validator_to = 'cosmosvaloper1urxrvt5dmkqpe50gwrerjly2z6nvk9exjz2j3h' then 'zoomerlabs'
     when validator_to = 'cosmosvaloper1ff0dw8kawsnxkrgj7p65kvw7jxxakyf8n583gx' then 'Compass'
     when validator_to = 'cosmosvaloper1v78emy9d2xe3tj974l7tmn2whca2nh9zp7s0u9' then 'a41'
     when validator_to = 'cosmosvaloper1kyfce0nvluyhgfsdzz8hwrsf5336gsc95pyy4u' then 'StakeSeeker by BTCS'
     when validator_to = 'cosmosvaloper1ed5a27kfyu0yljmna00vtr8mgzp6rwh9zn77zz' then 'CROSSTECH'
     when validator_to = 'cosmosvaloper1usvshtypjw57edkwxq3tagme665398f0hf4wuc' then 'Made In Block'
     when validator_to = 'cosmosvaloper1ha8d55747h8hsaluvz8ld88n24nfaw68rx4x92' then 'Lightning Capital'
     when validator_to = 'cosmosvaloper1wlpz5hau2ezu0gmuxav63m53d8s77az9wfzlt6' then '🤑 uGaenn ⛅'
     when validator_to = 'cosmosvaloper1zc0z44e42qhzltqc8qpj5qrzn836d3lftnqmgw' then 'Virtual Hive'
     when validator_to = 'cosmosvaloper1rj6324uq904z5zr96zg6ew9qjyau9u6h5nflg6' then 'Don Cryptonium'
     when validator_to = 'cosmosvaloper1yh089p0cre4nhpdqw35uzde5amg3qzexkeggdn' then 'High Stakes 🇨🇭'
     when validator_to = 'cosmosvaloper1a4qlael79p76my9pml6thwhnnzsxyy4ajrvd9s' then 'Multiplex'
     when validator_to = 'cosmosvaloper14upntdx8lf0f49t987mj99zksxnluanvu6x4lu' then 'Republic Crypto'
     when validator_to = 'cosmosvaloper1x3mkgqpshvpq87d33ndsleu7gd7w47dl4ve0yy' then 'CrowdControl'
     when validator_to = 'cosmosvaloper10f9wkd6vdspac05djyfwfx0uxcqxapnqhnkcg8' then 'Tavis Digital'
     when validator_to = 'cosmosvaloper1yfnaup5wa3vdzx3wx9auhvzl85saqj37tqxqnu' then 'Moonlet'
     when validator_to = 'cosmosvaloper1wdrypwex63geqswmcy5qynv4w3z3dyef2qmyna' then 'Genesis Lab'
     when validator_to = 'cosmosvaloper1de7qx00pz2j6gn9k88ntxxylelkazfk3g8fgh9' then 'Cosmic Validator | Auto-compound'
     when validator_to = 'cosmosvaloper1nxe3gnztx8wvayj260dp6yw7jg797m8up02h7z' then 'Synclub'
     when validator_to = 'cosmosvaloper1u6ddcsjueax884l3tfrs66497c7g86skn7pa0u' then 'Sentinel'
     when validator_to = 'cosmosvaloper1ec3p6a75mqwkv33zt543n6cnxqwun37rr5xlqv' then 'lunamint'
     when validator_to = 'cosmosvaloper1fun809ksxh87nzf88yashp9ynjz6xkscrtvzvw' then 'Tessellated'
     when validator_to = 'cosmosvaloper1gf3dm2mvqhymts6ksrstlyuu2m8pw6dhfp9md2' then 'Blockapsis'
     when validator_to = 'cosmosvaloper15r4tc0m6hc7z8drq3dzlrtcs6rq2q9l2nvwher' then 'DragonStake'
     when validator_to = 'cosmosvaloper1nz3c4q40j8jyvg2hcljkwhe69872mnllf7v9xh' then 'Interstellar Lounge'
     when validator_to = 'cosmosvaloper106yp7zw35wftheyyv9f9pe69t8rteumjrx52jg' then 'Bro_n_Bro'
     when validator_to = 'cosmosvaloper1v0g7guekttkdmerz5z8hjj8u8j68c6p00zqgf5' then 'LUNC DAO'
     when validator_to = 'cosmosvaloper12w6tynmjzq4l8zdla3v4x0jt8lt4rcz5gk7zg2' then 'Huobi-1'
     when validator_to = 'cosmosvaloper1d0aup392g3enru7eash83sedqclaxvp7fzh6gk' then 'Stir'
     when validator_to = 'cosmosvaloper1s05va5d09xlq3et8mapsesqh6r5lqy7mkhwshm' then 'Wetez'
     when validator_to = 'cosmosvaloper1n3nll7yl3lcv932s2r7l6jzvkjtjk0qppp3rls' then 'RoundTable21 by WildSage Labs'
    else 'Other' end as to_validator,
        case when validator_from = 'cosmosvaloper1sjllsnramtg3ewxqwwrwjxfgc4n4ef9u2lcnj0' then '1'
    when validator_from = 'cosmosvaloper1c4k24jzduc365kywrsvf5ujz4ya6mwympnc4en' then '2'
    when validator_from = 'cosmosvaloper14lultfckehtszvzw4ehu0apvsr77afvyju5zzy' then '3'
    when validator_from = 'cosmosvaloper1v5y0tg0jllvxf5c3afml8s3awue0ymju89frut' then '4'
    when validator_from = 'cosmosvaloper196ax4vc0lwpxndu9dyhvca7jhxp70rmcvrj90c' then '5'
    when validator_from = 'cosmosvaloper18ruzecmqj9pv8ac0gvkgryuc7u004te9rh7w5s' then '6'
    when validator_from = 'cosmosvaloper14k4pzckkre6uxxyd2lnhnpp8sngys9m6hl6ml7' then '7'
    when validator_from = 'cosmosvaloper1tflk30mq5vgqjdly92kkhhq3raev2hnz6eete3' then '8'
    when validator_from = 'cosmosvaloper1qaa9zej9a0ge3ugpx3pxyx602lxh3ztqgfnp42' then '9'
    when validator_from = 'cosmosvaloper19lss6zgdh5vvcpjhfftdghrpsw7a4434elpwpu' then '10'
    when validator_from = 'cosmosvaloper1ey69r37gfxvxg62sh4r0ktpuc46pzjrm873ae8' then '11'
    when validator_from = 'cosmosvaloper1hjct6q7npsspsg3dgvzk3sdf89spmlpfdn6m9d' then '12'
    when validator_from = 'cosmosvaloper1clpqr4nrk4khgkxj78fcwwh6dl3uw4epsluffn' then '13'
    when validator_from = 'cosmosvaloper156gqf9837u7d4c4678yt3rl4ls9c5vuursrrzf' then '14'
    when validator_from = 'cosmosvaloper132juzk0gdmwuxvx4phug7m3ymyatxlh9734g4w' then '15'
    when validator_from = 'cosmosvaloper15urq2dtp9qce4fyc85m6upwm9xul3049e02707' then '16'
    when validator_from = 'cosmosvaloper1z8zjv3lntpwxua0rtpvgrcwl0nm0tltgpgs6l7' then '17'
    when validator_from = 'cosmosvaloper1vf44d85es37hwl9f4h9gv0e064m0lla60j9luj' then '18'
    when validator_from = 'cosmosvaloper16k579jk6yt2cwmqx9dz5xvq9fug2tekvlu9qdv' then '19'
    when validator_from = 'cosmosvaloper1zqgheeawp7cmqk27dgyctd80rd8ryhqs6la9wc' then '20'
    when validator_from = 'cosmosvaloper1g48268mu5vfp4wk7dk89r0wdrakm9p5xk0q50k' then '21'
    when validator_from = 'cosmosvaloper1lzhlnpahvznwfv4jmay2tgaha5kmz5qxerarrl' then '22'
    when validator_from = 'cosmosvaloper1gpx52r9h3zeul45amvcy2pysgvcwddxrgx6cnv' then '23'
    when validator_from = 'cosmosvaloper1qwl879nx9t6kef4supyazayf7vjhennyh568ys' then '24'
    when validator_from = 'cosmosvaloper1gdg6qqe5a3u483unqlqsnullja23g0xvqkxtk0' then '25'
    when validator_from = 'cosmosvaloper1n229vhepft6wnkt5tjpwmxdmcnfz55jv3vp77d' then '26'
    when validator_from = 'cosmosvaloper1ma02nlc7lchu7caufyrrqt4r6v2mpsj90y9wzd' then '27'
    when validator_from = 'cosmosvaloper1vvwtk805lxehwle9l4yudmq6mn0g32px9xtkhc' then '28'
    when validator_from = 'cosmosvaloper1eh5mwu044gd5ntkkc2xgfg8247mgc56fz4sdg3' then '29'
    when validator_from = 'cosmosvaloper1grgelyng2v6v3t8z87wu3sxgt9m5s03xfytvz7' then '30'
    when validator_from = 'cosmosvaloper1te8nxpc2myjfrhaty0dnzdhs5ahdh5agzuym9v' then '31'
    when validator_from = 'cosmosvaloper1rpgtz9pskr5geavkjz02caqmeep7cwwpv73axj' then '32'
    when validator_from = 'cosmosvaloper14kn0kk33szpwus9nh8n87fjel8djx0y070ymmj' then '33'
    when validator_from = 'cosmosvaloper1y0us8xvsvfvqkk9c6nt5cfyu5au5tww2ztve7q' then '34'
    when validator_from = 'cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p' then '35'
    when validator_from = 'cosmosvaloper130mdu9a0etmeuw52qfxk73pn0ga6gawkxsrlwf' then '36'
    when validator_from = 'cosmosvaloper16fnz0v4cnv5dpnj0p3gaft2q2kzx8z5hfrx6v5' then '37'
    when validator_from = 'cosmosvaloper1we6knm8qartmmh2r0qfpsz6pq0s7emv3e0meuw' then '38'
    when validator_from = 'cosmosvaloper1jst8q8flpn94u9uvkpae8mrkk3a5pjhxx529z2' then '39'
    when validator_from = 'cosmosvaloper10e4vsut6suau8tk9m6dnrm0slgd6npe3jx5xpv' then '40'
    when validator_from = 'cosmosvaloper1kgddca7qj96z0qcxr2c45z73cfl0c75p7f3s2e' then '41'
    when validator_from = 'cosmosvaloper1cc99d3xcukhedg4wcw53j7a9q68uza707vpfe7' then '42'
    when validator_from = 'cosmosvaloper19rmlxkqjt950fxl849l49x0me56u9tkd5n5j62' then '43'
    when validator_from = 'cosmosvaloper199mlc7fr6ll5t54w7tts7f4s0cvnqgc59nmuxf' then '44'
    when validator_from = 'cosmosvaloper1k2d9ed9vgfuk2m58a2d80q9u6qljkh4vfaqjfq' then '45'
    when validator_from = 'cosmosvaloper10wljxpl03053h9690apmyeakly3ylhejrucvtm' then '46'
    when validator_from = 'cosmosvaloper1uutuwrwt3z2a5z8z3uasml3rftlpmu25aga5c6' then '47'
    when validator_from = 'cosmosvaloper1ssm0d433seakyak8kcf93yefhknjleeds4y3em' then '48'
    when validator_from = 'cosmosvaloper1ehkfl7palwrh6w2hhr2yfrgrq8jetgucudztfe' then '49'
    when validator_from = 'cosmosvaloper19yy989ka5usws6gsd8vl94y7l6ssgdwsrnscjc' then '50'
    when validator_from = 'cosmosvaloper1hjadhj9nqzpye2vkmkz4thahhd0z8dh3udhq74' then '51'
    when validator_from = 'cosmosvaloper157v7tczs40axfgejp2m43kwuzqe0wsy0rv8puv' then '52'
    when validator_from = 'cosmosvaloper1gxju9ky3hwxvqqagrl3dxtl49kjpxq6wlqe6m5' then '53'
    when validator_from = 'cosmosvaloper1n3mhyp9fvcmuu8l0q8qvjy07x0rql8q46fe2xk' then '54'
    when validator_from = 'cosmosvaloper146kwpzhmleafmhtaxulfptyhnvwxzlvm87hwnm' then '55'
    when validator_from = 'cosmosvaloper1x8efhljzvs52u5xa6m7crcwes7v9u0nlwdgw30' then '56'
    when validator_from = 'cosmosvaloper14l0fp639yudfl46zauvv8rkzjgd4u0zk2aseys' then '57'
    when validator_from = 'cosmosvaloper13nvnv6q8d3yg7tjeahjzljkqu0y27s8y9e7as9' then '58'
    when validator_from = 'cosmosvaloper1dqp325was50l7ut2lnx6s8xhmtwj3wrtx06gzu' then '59'
    when validator_from = 'cosmosvaloper1lktjhnzkpkz3ehrg8psvmwhafg56kfss3q3t8m' then '60'
    when validator_from = 'cosmosvaloper1udpsgkgyutgsglauk9vk9rs03a3skc62gup9ny' then '61'
    when validator_from = 'cosmosvaloper10nzaaeh2kq28t3nqsh5m8kmyv90vx7ym5mpakx' then '62'
    when validator_from = 'cosmosvaloper1sd4tl9aljmmezzudugs7zlaya7pg2895ws8tfs' then '63'
    when validator_from = 'cosmosvaloper124maqmcqv8tquy764ktz7cu0gxnzfw54n3vww8' then '64'
    when validator_from = 'cosmosvaloper1uhnsxv6m83jj3328mhrql7yax3nge5svrv6t6c' then '65'
    when validator_from = 'cosmosvaloper1ptyzewnns2kn37ewtmv6ppsvhdnmeapvtfc9y5' then '66'
    when validator_from = 'cosmosvaloper157qezau9xnzypse3vu2vhs7r4ee83fdecew0fz' then '67'
    when validator_from = 'cosmosvaloper1ul2me6vukg2vac2p6ltxmqlaa7jywdgt8q76ag' then '68'
    when validator_from = 'cosmosvaloper17mggn4znyeyg25wd7498qxl7r2jhgue8u4qjcq' then '69'
    when validator_from = 'cosmosvaloper1q6d3d089hg59x6gcx92uumx70s5y5wadklue8s' then '70'
    when validator_from = 'cosmosvaloper1sxx9mszve0gaedz5ld7qdkjkfv8z992ax69k08' then '71'
    when validator_from = 'cosmosvaloper1lcwxu50rvvgf9v6jy6q5mrzyhlszwtjxhtscmp' then '72'
    when validator_from = 'cosmosvaloper1dt93l3qgmhhlp97srjyqyendrgu9nx0suxtwe8' then '73'
    when validator_from = 'cosmosvaloper1ej2es5fjztqjcd4pwa0zyvaevtjd2y5wxxp9gd' then '74'
    when validator_from = 'cosmosvaloper1gjtvly9lel6zskvwtvlg5vhwpu9c9waw7sxzwx' then '75'
    when validator_from = 'cosmosvaloper1r2dthxctqzhwg299e7aaeqwfkgcc9hg8k3yd7m' then '76'
    when validator_from = 'cosmosvaloper1pjmngrwcsatsuyy8m3qrunaun67sr9x7z5r2qs' then '77'
    when validator_from = 'cosmosvaloper10jzj3jjd3frna0ay08sh4zu4fpy957s49jkk7m' then '78'
    when validator_from = 'cosmosvaloper1m73mgwn3cm2e8x9a9axa0kw8nqz8a492ms63vn' then '79'
    when validator_from = 'cosmosvaloper1symf474wnypes2d3mecllqk6l26rwz8mfjqdus' then '80'
    when validator_from = 'cosmosvaloper1hdrlqvyjfy5sdrseecjrutyws9khtxxaux62l7' then '81'
    when validator_from = 'cosmosvaloper17h2x3j7u44qkrq0sk8ul0r2qr440rwgjkfg0gh' then '82'
    when validator_from = 'cosmosvaloper1gf4wlkutql95j7wwsxz490s6fahlvk2s9xpwax' then '83'
    when validator_from = 'cosmosvaloper1cgh5ksjwy2sd407lyre4l3uj2fdrqhpkzp06e6' then '84'
    when validator_from = 'cosmosvaloper13sduv92y3xdhy3rpmhakrc3v7t37e7ps9l0kpv' then '85'
    when validator_from = 'cosmosvaloper1gp957czryfgyvxwn3tfnyy2f0t9g2p4pqeemx8' then '86'
    when validator_from = 'cosmosvaloper1083svrca4t350mphfv9x45wq9asrs60cdmrflj' then '87'
    when validator_from = 'cosmosvaloper1nuhls0wyf8slhmuasha5pz0u89jrf9nnugq8ak' then '88'
    when validator_from = 'cosmosvaloper1x8rr4hcf54nz6hfckyy2n05sxss54h8wz9puzg' then '89'
    when validator_from = 'cosmosvaloper1thl5syhmscgnj7whdyrydw3w6vy80044hjpnxh' then '90'
    when validator_from = 'cosmosvaloper1keltez56g3zm9w8wr8gcmmulze48g2q3usuw8c' then '91'
    when validator_from = 'cosmosvaloper140l6y2gp3gxvay6qtn70re7z2s0gn57zfd832j' then '92'
    when validator_from = 'cosmosvaloper1ddle9tczl87gsvmeva3c48nenyng4n56nghmjk' then '93'
    when validator_from = 'cosmosvaloper1rwh0cxa72d3yle3r4l8gd7vyphrmjy2kpe4x72' then '94'
    when validator_from = 'cosmosvaloper19ecn7ljwp6el2pc5lldyauwv05ufwut9mm38r5' then '95'
    when validator_from = 'cosmosvaloper1fhr7e04ct0zslmkzqt9smakg3sxrdve6ulclj2' then '96'
    when validator_from = 'cosmosvaloper1jlr62guqwrwkdt4m3y00zh2rrsamhjf9num5xr' then '97'
    when validator_from = 'cosmosvaloper122j3zmqdl6d2g64qmjuqzj65gfejsvjp07yljn' then '98'
    when validator_from = 'cosmosvaloper1xym2qygmr9vanpa0m7ndk3n0qxgey3ffzcyd5c' then '99'
    when validator_from = 'cosmosvaloper1e4vye322gkjx8n85jgcclnc7nvdvu82axnr5ll' then '100'
    when validator_from = 'cosmosvaloper13maqgtlklmereflvg3lq3e8zrp0jsqhr8ef3kk' then '101'
    when validator_from = 'cosmosvaloper1kn3wugetjuy4zetlq6wadchfhvu3x740ae6z6x' then '102'
    when validator_from = 'cosmosvaloper1svwt2mr4x2mx0hcmty0mxsa4rmlfau4lwx2l69' then '103'
    when validator_from = 'cosmosvaloper1wrx0x9m9ykdhw9sg04v7uljme53wuj03aa5d4f' then '104'
    when validator_from = 'cosmosvaloper16yupepagywvlk7uhpfchtwa0stu5f8cyhh54f2' then '105'
    when validator_from = 'cosmosvaloper18extdhzzl5c8tr6453e5hzaj3exrdlea90fj3y' then '106'
    when validator_from = 'cosmosvaloper1e859xaue4k2jzqw20cv6l7p3tmc378pc3k8g2u' then '107'
    when validator_from = 'cosmosvaloper1rcp29q3hpd246n6qak7jluqep4v006cdsc2kkl' then '108'
    when validator_from = 'cosmosvaloper1vygmh344ldv9qefss9ek7ggsnxparljlmj56q5' then '109'
    when validator_from = 'cosmosvaloper16s96n9k9zztdgjy8q4qcxp4hn7ww98qkrka4zk' then '110'
    when validator_from = 'cosmosvaloper1wqy2s6nwnxj57l0l5rdjxxr646p3al6y70435m' then '111'
    when validator_from = 'cosmosvaloper1xnrth5rku3z3msm9prxe3l0p2yec3d9mzxz9ka' then '112'
    when validator_from = 'cosmosvaloper102ruvpv2srmunfffxavttxnhezln6fnc54at8c' then '113'
    when validator_from = 'cosmosvaloper1fsg635n5vgc7jazz9sx5725wnc3xqgr7awxaag' then '114'
    when validator_from = 'cosmosvaloper1xwazl8ftks4gn00y5x3c47auquc62ssuqlj02r' then '115'
    when validator_from = 'cosmosvaloper1e0plfg475phrsvrlzw8gwppeva0zk5yg9fgg8c' then '116'
    when validator_from = 'cosmosvaloper10unx6s0cdqntvrumd5hs07rgd5ytcztqh8etw6' then '117'
    when validator_from = 'cosmosvaloper1fqzqejwkk898fcslw4z4eeqjzesynvrdfr5hte' then '118'
    when validator_from = 'cosmosvaloper142w8q2l0gxsfna72gq8t7e4ee4ul37e9htgtxx' then '119'
    when validator_from = 'cosmosvaloper1jmykcq8gylmy5tgqtel4xj4q62fdt49sl584xd' then '120'
    when validator_from = 'cosmosvaloper16qme5yxucnaj6snx35nmwze0wyxr8wfgqxsqfw' then '121'
    when validator_from = 'cosmosvaloper1aewyh4gtvayx6v7w592jdfylawk4rsu9tfvfgm' then '122'
    when validator_from = 'cosmosvaloper125umsz3fws7gepn5ccsh0sv4gre9r6a3tccz4r' then '123'
    when validator_from = 'cosmosvaloper14qazscc80zgzx3m0m0aa30ths0p9hg8vdglqrc' then '124'
    when validator_from = 'cosmosvaloper1et77usu8q2hargvyusl4qzryev8x8t9wwqkxfs' then '125'
    when validator_from = 'cosmosvaloper1485u80fdxjan4sd3esrvyw6cyurpvddvzuh48y' then '126'
    when validator_from = 'cosmosvaloper1yw5s259jkcg0jzmh7sce29uk0lqqw2ump7578p' then '127'
    when validator_from = 'cosmosvaloper1lkujuk2004p3w42tgvuvqnsdmsq8u6jqkwf9wj' then '128'
    when validator_from = 'cosmosvaloper140e7u946a2nqqkvcnjpjm83d0ynsqem8dnp684' then '129'
    when validator_from = 'cosmosvaloper13x77yexvf6qexfjg9czp6jhpv7vpjdwwkyhe4p' then '130'
    when validator_from = 'cosmosvaloper1jxv0u20scum4trha72c7ltfgfqef6nsch7q6cu' then '131'
    when validator_from = 'cosmosvaloper1qs8tnw2t8l6amtzvdemnnsq9dzk0ag0z52uzay' then '132'
    when validator_from = 'cosmosvaloper1z66j0z75a9flwnez7sa8jxx46cqu4rfhd9q82w' then '133'
    when validator_from = 'cosmosvaloper1648ynlpdw7fqa2axt0w2yp3fk542junl7rsvq6' then '134'
    when validator_from = 'cosmosvaloper1j0vaeh27t4rll7zhmarwcuq8xtrmvqhudrgcky' then '135'
    when validator_from = 'cosmosvaloper1v69lzl909kje64k8vae24uytpxcnpxgullz2dx' then '136'
    when validator_from = 'cosmosvaloper103agss48504gkk3la5xcg5kxplaf6ttnuv234h' then '137'
    when validator_from = 'cosmosvaloper1sdz4rc95vnzh2f54sacec50vjxnmwdakfym4vh' then '138'
    when validator_from = 'cosmosvaloper12lfqufkk2h3w2ycp50czme6nj3ln5tdv7nj3hx' then '139'
    when validator_from = 'cosmosvaloper1crqm3598z6qmyn2kkcl9dz7uqs4qdqnr6s8jdn' then '140'
    when validator_from = 'cosmosvaloper1ukpah0340rx7k3x2njnavwyjv6pfpvn632df9q' then '141'
    when validator_from = 'cosmosvaloper1ualhu3fjgg77g485gmyswkq3w0dp7gys6qzwrv' then '142'
    when validator_from = 'cosmosvaloper13ql36flc4cdjhx08hke5vpr4dyv03aafnmvtnc' then '143'
    when validator_from = 'cosmosvaloper1urxrvt5dmkqpe50gwrerjly2z6nvk9exjz2j3h' then '144'
    when validator_from = 'cosmosvaloper1ff0dw8kawsnxkrgj7p65kvw7jxxakyf8n583gx' then '145'
    when validator_from = 'cosmosvaloper1v78emy9d2xe3tj974l7tmn2whca2nh9zp7s0u9' then '146'
    when validator_from = 'cosmosvaloper1kyfce0nvluyhgfsdzz8hwrsf5336gsc95pyy4u' then '147'
    when validator_from = 'cosmosvaloper1ed5a27kfyu0yljmna00vtr8mgzp6rwh9zn77zz' then '148'
    when validator_from = 'cosmosvaloper1usvshtypjw57edkwxq3tagme665398f0hf4wuc' then '149'
    when validator_from = 'cosmosvaloper1ha8d55747h8hsaluvz8ld88n24nfaw68rx4x92' then '150'
    when validator_from = 'cosmosvaloper1wlpz5hau2ezu0gmuxav63m53d8s77az9wfzlt6' then '151'
    when validator_from = 'cosmosvaloper1zc0z44e42qhzltqc8qpj5qrzn836d3lftnqmgw' then '152'
    when validator_from = 'cosmosvaloper1rj6324uq904z5zr96zg6ew9qjyau9u6h5nflg6' then '153'
    when validator_from = 'cosmosvaloper1yh089p0cre4nhpdqw35uzde5amg3qzexkeggdn' then '154'
    when validator_from = 'cosmosvaloper1a4qlael79p76my9pml6thwhnnzsxyy4ajrvd9s' then '155'
    when validator_from = 'cosmosvaloper14upntdx8lf0f49t987mj99zksxnluanvu6x4lu' then '156'
    when validator_from = 'cosmosvaloper1x3mkgqpshvpq87d33ndsleu7gd7w47dl4ve0yy' then '157'
    when validator_from = 'cosmosvaloper10f9wkd6vdspac05djyfwfx0uxcqxapnqhnkcg8' then '158'
    when validator_from = 'cosmosvaloper1yfnaup5wa3vdzx3wx9auhvzl85saqj37tqxqnu' then '159'
    when validator_from = 'cosmosvaloper1wdrypwex63geqswmcy5qynv4w3z3dyef2qmyna' then '160'
    when validator_from = 'cosmosvaloper1de7qx00pz2j6gn9k88ntxxylelkazfk3g8fgh9' then '161'
    when validator_from = 'cosmosvaloper1nxe3gnztx8wvayj260dp6yw7jg797m8up02h7z' then '162'
    when validator_from = 'cosmosvaloper1u6ddcsjueax884l3tfrs66497c7g86skn7pa0u' then '163'
    when validator_from = 'cosmosvaloper1ec3p6a75mqwkv33zt543n6cnxqwun37rr5xlqv' then '164'
    when validator_from = 'cosmosvaloper1fun809ksxh87nzf88yashp9ynjz6xkscrtvzvw' then '165'
    when validator_from = 'cosmosvaloper1gf3dm2mvqhymts6ksrstlyuu2m8pw6dhfp9md2' then '166'
    when validator_from = 'cosmosvaloper15r4tc0m6hc7z8drq3dzlrtcs6rq2q9l2nvwher' then '167'
    when validator_from = 'cosmosvaloper1nz3c4q40j8jyvg2hcljkwhe69872mnllf7v9xh' then '168'
    when validator_from = 'cosmosvaloper106yp7zw35wftheyyv9f9pe69t8rteumjrx52jg' then '169'
    when validator_from = 'cosmosvaloper1v0g7guekttkdmerz5z8hjj8u8j68c6p00zqgf5' then '170'
    when validator_from = 'cosmosvaloper12w6tynmjzq4l8zdla3v4x0jt8lt4rcz5gk7zg2' then '171'
    when validator_from = 'cosmosvaloper1d0aup392g3enru7eash83sedqclaxvp7fzh6gk' then '172'
    when validator_from = 'cosmosvaloper1s05va5d09xlq3et8mapsesqh6r5lqy7mkhwshm' then '173'
    when validator_from = 'cosmosvaloper1n3nll7yl3lcv932s2r7l6jzvkjtjk0qppp3rls' then '174'
    else '200' end as from_validator_rank,
      
    case when c.validator_to = 'cosmosvaloper1sjllsnramtg3ewxqwwrwjxfgc4n4ef9u2lcnj0' then '1'
    when c.validator_to = 'cosmosvaloper1c4k24jzduc365kywrsvf5ujz4ya6mwympnc4en' then '2'
    when c.validator_to = 'cosmosvaloper14lultfckehtszvzw4ehu0apvsr77afvyju5zzy' then '3'
    when c.validator_to = 'cosmosvaloper1v5y0tg0jllvxf5c3afml8s3awue0ymju89frut' then '4'
    when c.validator_to = 'cosmosvaloper196ax4vc0lwpxndu9dyhvca7jhxp70rmcvrj90c' then '5'
    when c.validator_to = 'cosmosvaloper18ruzecmqj9pv8ac0gvkgryuc7u004te9rh7w5s' then '6'
    when c.validator_to = 'cosmosvaloper14k4pzckkre6uxxyd2lnhnpp8sngys9m6hl6ml7' then '7'
    when c.validator_to = 'cosmosvaloper1tflk30mq5vgqjdly92kkhhq3raev2hnz6eete3' then '8'
    when c.validator_to = 'cosmosvaloper1qaa9zej9a0ge3ugpx3pxyx602lxh3ztqgfnp42' then '9'
    when c.validator_to = 'cosmosvaloper19lss6zgdh5vvcpjhfftdghrpsw7a4434elpwpu' then '10'
    when c.validator_to = 'cosmosvaloper1ey69r37gfxvxg62sh4r0ktpuc46pzjrm873ae8' then '11'
    when c.validator_to = 'cosmosvaloper1hjct6q7npsspsg3dgvzk3sdf89spmlpfdn6m9d' then '12'
    when c.validator_to = 'cosmosvaloper1clpqr4nrk4khgkxj78fcwwh6dl3uw4epsluffn' then '13'
    when c.validator_to = 'cosmosvaloper156gqf9837u7d4c4678yt3rl4ls9c5vuursrrzf' then '14'
    when c.validator_to = 'cosmosvaloper132juzk0gdmwuxvx4phug7m3ymyatxlh9734g4w' then '15'
    when c.validator_to = 'cosmosvaloper15urq2dtp9qce4fyc85m6upwm9xul3049e02707' then '16'
    when c.validator_to = 'cosmosvaloper1z8zjv3lntpwxua0rtpvgrcwl0nm0tltgpgs6l7' then '17'
    when c.validator_to = 'cosmosvaloper1vf44d85es37hwl9f4h9gv0e064m0lla60j9luj' then '18'
    when c.validator_to = 'cosmosvaloper16k579jk6yt2cwmqx9dz5xvq9fug2tekvlu9qdv' then '19'
    when c.validator_to = 'cosmosvaloper1zqgheeawp7cmqk27dgyctd80rd8ryhqs6la9wc' then '20'
    when c.validator_to = 'cosmosvaloper1g48268mu5vfp4wk7dk89r0wdrakm9p5xk0q50k' then '21'
    when c.validator_to = 'cosmosvaloper1lzhlnpahvznwfv4jmay2tgaha5kmz5qxerarrl' then '22'
    when c.validator_to = 'cosmosvaloper1gpx52r9h3zeul45amvcy2pysgvcwddxrgx6cnv' then '23'
    when c.validator_to = 'cosmosvaloper1qwl879nx9t6kef4supyazayf7vjhennyh568ys' then '24'
    when c.validator_to = 'cosmosvaloper1gdg6qqe5a3u483unqlqsnullja23g0xvqkxtk0' then '25'
    when c.validator_to = 'cosmosvaloper1n229vhepft6wnkt5tjpwmxdmcnfz55jv3vp77d' then '26'
    when c.validator_to = 'cosmosvaloper1ma02nlc7lchu7caufyrrqt4r6v2mpsj90y9wzd' then '27'
    when c.validator_to = 'cosmosvaloper1vvwtk805lxehwle9l4yudmq6mn0g32px9xtkhc' then '28'
    when c.validator_to = 'cosmosvaloper1eh5mwu044gd5ntkkc2xgfg8247mgc56fz4sdg3' then '29'
    when c.validator_to = 'cosmosvaloper1grgelyng2v6v3t8z87wu3sxgt9m5s03xfytvz7' then '30'
    when c.validator_to = 'cosmosvaloper1te8nxpc2myjfrhaty0dnzdhs5ahdh5agzuym9v' then '31'
    when c.validator_to = 'cosmosvaloper1rpgtz9pskr5geavkjz02caqmeep7cwwpv73axj' then '32'
    when c.validator_to = 'cosmosvaloper14kn0kk33szpwus9nh8n87fjel8djx0y070ymmj' then '33'
    when c.validator_to = 'cosmosvaloper1y0us8xvsvfvqkk9c6nt5cfyu5au5tww2ztve7q' then '34'
    when c.validator_to = 'cosmosvaloper1x88j7vp2xnw3zec8ur3g4waxycyz7m0mahdv3p' then '35'
    when c.validator_to = 'cosmosvaloper130mdu9a0etmeuw52qfxk73pn0ga6gawkxsrlwf' then '36'
    when c.validator_to = 'cosmosvaloper16fnz0v4cnv5dpnj0p3gaft2q2kzx8z5hfrx6v5' then '37'
    when c.validator_to = 'cosmosvaloper1we6knm8qartmmh2r0qfpsz6pq0s7emv3e0meuw' then '38'
    when c.validator_to = 'cosmosvaloper1jst8q8flpn94u9uvkpae8mrkk3a5pjhxx529z2' then '39'
    when c.validator_to = 'cosmosvaloper10e4vsut6suau8tk9m6dnrm0slgd6npe3jx5xpv' then '40'
    when c.validator_to = 'cosmosvaloper1kgddca7qj96z0qcxr2c45z73cfl0c75p7f3s2e' then '41'
    when c.validator_to = 'cosmosvaloper1cc99d3xcukhedg4wcw53j7a9q68uza707vpfe7' then '42'
    when c.validator_to = 'cosmosvaloper19rmlxkqjt950fxl849l49x0me56u9tkd5n5j62' then '43'
    when c.validator_to = 'cosmosvaloper199mlc7fr6ll5t54w7tts7f4s0cvnqgc59nmuxf' then '44'
    when c.validator_to = 'cosmosvaloper1k2d9ed9vgfuk2m58a2d80q9u6qljkh4vfaqjfq' then '45'
    when c.validator_to = 'cosmosvaloper10wljxpl03053h9690apmyeakly3ylhejrucvtm' then '46'
    when c.validator_to = 'cosmosvaloper1uutuwrwt3z2a5z8z3uasml3rftlpmu25aga5c6' then '47'
    when c.validator_to = 'cosmosvaloper1ssm0d433seakyak8kcf93yefhknjleeds4y3em' then '48'
    when c.validator_to = 'cosmosvaloper1ehkfl7palwrh6w2hhr2yfrgrq8jetgucudztfe' then '49'
    when c.validator_to = 'cosmosvaloper19yy989ka5usws6gsd8vl94y7l6ssgdwsrnscjc' then '50'
    when c.validator_to = 'cosmosvaloper1hjadhj9nqzpye2vkmkz4thahhd0z8dh3udhq74' then '51'
    when c.validator_to = 'cosmosvaloper157v7tczs40axfgejp2m43kwuzqe0wsy0rv8puv' then '52'
    when c.validator_to = 'cosmosvaloper1gxju9ky3hwxvqqagrl3dxtl49kjpxq6wlqe6m5' then '53'
    when c.validator_to = 'cosmosvaloper1n3mhyp9fvcmuu8l0q8qvjy07x0rql8q46fe2xk' then '54'
    when c.validator_to = 'cosmosvaloper146kwpzhmleafmhtaxulfptyhnvwxzlvm87hwnm' then '55'
    when c.validator_to = 'cosmosvaloper1x8efhljzvs52u5xa6m7crcwes7v9u0nlwdgw30' then '56'
    when c.validator_to = 'cosmosvaloper14l0fp639yudfl46zauvv8rkzjgd4u0zk2aseys' then '57'
    when c.validator_to = 'cosmosvaloper13nvnv6q8d3yg7tjeahjzljkqu0y27s8y9e7as9' then '58'
    when c.validator_to = 'cosmosvaloper1dqp325was50l7ut2lnx6s8xhmtwj3wrtx06gzu' then '59'
    when c.validator_to = 'cosmosvaloper1lktjhnzkpkz3ehrg8psvmwhafg56kfss3q3t8m' then '60'
    when c.validator_to = 'cosmosvaloper1udpsgkgyutgsglauk9vk9rs03a3skc62gup9ny' then '61'
    when c.validator_to = 'cosmosvaloper10nzaaeh2kq28t3nqsh5m8kmyv90vx7ym5mpakx' then '62'
    when c.validator_to = 'cosmosvaloper1sd4tl9aljmmezzudugs7zlaya7pg2895ws8tfs' then '63'
    when c.validator_to = 'cosmosvaloper124maqmcqv8tquy764ktz7cu0gxnzfw54n3vww8' then '64'
    when c.validator_to = 'cosmosvaloper1uhnsxv6m83jj3328mhrql7yax3nge5svrv6t6c' then '65'
    when c.validator_to = 'cosmosvaloper1ptyzewnns2kn37ewtmv6ppsvhdnmeapvtfc9y5' then '66'
    when c.validator_to = 'cosmosvaloper157qezau9xnzypse3vu2vhs7r4ee83fdecew0fz' then '67'
    when c.validator_to = 'cosmosvaloper1ul2me6vukg2vac2p6ltxmqlaa7jywdgt8q76ag' then '68'
    when c.validator_to = 'cosmosvaloper17mggn4znyeyg25wd7498qxl7r2jhgue8u4qjcq' then '69'
    when c.validator_to = 'cosmosvaloper1q6d3d089hg59x6gcx92uumx70s5y5wadklue8s' then '70'
    when c.validator_to = 'cosmosvaloper1sxx9mszve0gaedz5ld7qdkjkfv8z992ax69k08' then '71'
    when c.validator_to = 'cosmosvaloper1lcwxu50rvvgf9v6jy6q5mrzyhlszwtjxhtscmp' then '72'
    when c.validator_to = 'cosmosvaloper1dt93l3qgmhhlp97srjyqyendrgu9nx0suxtwe8' then '73'
    when c.validator_to = 'cosmosvaloper1ej2es5fjztqjcd4pwa0zyvaevtjd2y5wxxp9gd' then '74'
    when c.validator_to = 'cosmosvaloper1gjtvly9lel6zskvwtvlg5vhwpu9c9waw7sxzwx' then '75'
    when c.validator_to = 'cosmosvaloper1r2dthxctqzhwg299e7aaeqwfkgcc9hg8k3yd7m' then '76'
    when c.validator_to = 'cosmosvaloper1pjmngrwcsatsuyy8m3qrunaun67sr9x7z5r2qs' then '77'
    when c.validator_to = 'cosmosvaloper10jzj3jjd3frna0ay08sh4zu4fpy957s49jkk7m' then '78'
    when c.validator_to = 'cosmosvaloper1m73mgwn3cm2e8x9a9axa0kw8nqz8a492ms63vn' then '79'
    when c.validator_to = 'cosmosvaloper1symf474wnypes2d3mecllqk6l26rwz8mfjqdus' then '80'
    when c.validator_to = 'cosmosvaloper1hdrlqvyjfy5sdrseecjrutyws9khtxxaux62l7' then '81'
    when c.validator_to = 'cosmosvaloper17h2x3j7u44qkrq0sk8ul0r2qr440rwgjkfg0gh' then '82'
    when c.validator_to = 'cosmosvaloper1gf4wlkutql95j7wwsxz490s6fahlvk2s9xpwax' then '83'
    when c.validator_to = 'cosmosvaloper1cgh5ksjwy2sd407lyre4l3uj2fdrqhpkzp06e6' then '84'
    when c.validator_to = 'cosmosvaloper13sduv92y3xdhy3rpmhakrc3v7t37e7ps9l0kpv' then '85'
    when c.validator_to = 'cosmosvaloper1gp957czryfgyvxwn3tfnyy2f0t9g2p4pqeemx8' then '86'
    when c.validator_to = 'cosmosvaloper1083svrca4t350mphfv9x45wq9asrs60cdmrflj' then '87'
    when c.validator_to = 'cosmosvaloper1nuhls0wyf8slhmuasha5pz0u89jrf9nnugq8ak' then '88'
    when c.validator_to = 'cosmosvaloper1x8rr4hcf54nz6hfckyy2n05sxss54h8wz9puzg' then '89'
    when c.validator_to = 'cosmosvaloper1thl5syhmscgnj7whdyrydw3w6vy80044hjpnxh' then '90'
    when c.validator_to = 'cosmosvaloper1keltez56g3zm9w8wr8gcmmulze48g2q3usuw8c' then '91'
    when c.validator_to = 'cosmosvaloper140l6y2gp3gxvay6qtn70re7z2s0gn57zfd832j' then '92'
    when c.validator_to = 'cosmosvaloper1ddle9tczl87gsvmeva3c48nenyng4n56nghmjk' then '93'
    when c.validator_to = 'cosmosvaloper1rwh0cxa72d3yle3r4l8gd7vyphrmjy2kpe4x72' then '94'
    when c.validator_to = 'cosmosvaloper19ecn7ljwp6el2pc5lldyauwv05ufwut9mm38r5' then '95'
    when c.validator_to = 'cosmosvaloper1fhr7e04ct0zslmkzqt9smakg3sxrdve6ulclj2' then '96'
    when c.validator_to = 'cosmosvaloper1jlr62guqwrwkdt4m3y00zh2rrsamhjf9num5xr' then '97'
    when c.validator_to = 'cosmosvaloper122j3zmqdl6d2g64qmjuqzj65gfejsvjp07yljn' then '98'
    when c.validator_to = 'cosmosvaloper1xym2qygmr9vanpa0m7ndk3n0qxgey3ffzcyd5c' then '99'
    when c.validator_to = 'cosmosvaloper1e4vye322gkjx8n85jgcclnc7nvdvu82axnr5ll' then '100'
    when c.validator_to = 'cosmosvaloper13maqgtlklmereflvg3lq3e8zrp0jsqhr8ef3kk' then '101'
    when c.validator_to = 'cosmosvaloper1kn3wugetjuy4zetlq6wadchfhvu3x740ae6z6x' then '102'
    when c.validator_to = 'cosmosvaloper1svwt2mr4x2mx0hcmty0mxsa4rmlfau4lwx2l69' then '103'
    when c.validator_to = 'cosmosvaloper1wrx0x9m9ykdhw9sg04v7uljme53wuj03aa5d4f' then '104'
    when c.validator_to = 'cosmosvaloper16yupepagywvlk7uhpfchtwa0stu5f8cyhh54f2' then '105'
    when c.validator_to = 'cosmosvaloper18extdhzzl5c8tr6453e5hzaj3exrdlea90fj3y' then '106'
    when c.validator_to = 'cosmosvaloper1e859xaue4k2jzqw20cv6l7p3tmc378pc3k8g2u' then '107'
    when c.validator_to = 'cosmosvaloper1rcp29q3hpd246n6qak7jluqep4v006cdsc2kkl' then '108'
    when c.validator_to = 'cosmosvaloper1vygmh344ldv9qefss9ek7ggsnxparljlmj56q5' then '109'
    when c.validator_to = 'cosmosvaloper16s96n9k9zztdgjy8q4qcxp4hn7ww98qkrka4zk' then '110'
    when c.validator_to = 'cosmosvaloper1wqy2s6nwnxj57l0l5rdjxxr646p3al6y70435m' then '111'
    when c.validator_to = 'cosmosvaloper1xnrth5rku3z3msm9prxe3l0p2yec3d9mzxz9ka' then '112'
    when c.validator_to = 'cosmosvaloper102ruvpv2srmunfffxavttxnhezln6fnc54at8c' then '113'
    when c.validator_to = 'cosmosvaloper1fsg635n5vgc7jazz9sx5725wnc3xqgr7awxaag' then '114'
    when c.validator_to = 'cosmosvaloper1xwazl8ftks4gn00y5x3c47auquc62ssuqlj02r' then '115'
    when c.validator_to = 'cosmosvaloper1e0plfg475phrsvrlzw8gwppeva0zk5yg9fgg8c' then '116'
    when c.validator_to = 'cosmosvaloper10unx6s0cdqntvrumd5hs07rgd5ytcztqh8etw6' then '117'
    when c.validator_to = 'cosmosvaloper1fqzqejwkk898fcslw4z4eeqjzesynvrdfr5hte' then '118'
    when c.validator_to = 'cosmosvaloper142w8q2l0gxsfna72gq8t7e4ee4ul37e9htgtxx' then '119'
    when c.validator_to = 'cosmosvaloper1jmykcq8gylmy5tgqtel4xj4q62fdt49sl584xd' then '120'
    when c.validator_to = 'cosmosvaloper16qme5yxucnaj6snx35nmwze0wyxr8wfgqxsqfw' then '121'
    when c.validator_to = 'cosmosvaloper1aewyh4gtvayx6v7w592jdfylawk4rsu9tfvfgm' then '122'
    when c.validator_to = 'cosmosvaloper125umsz3fws7gepn5ccsh0sv4gre9r6a3tccz4r' then '123'
    when c.validator_to = 'cosmosvaloper14qazscc80zgzx3m0m0aa30ths0p9hg8vdglqrc' then '124'
    when c.validator_to = 'cosmosvaloper1et77usu8q2hargvyusl4qzryev8x8t9wwqkxfs' then '125'
    when c.validator_to = 'cosmosvaloper1485u80fdxjan4sd3esrvyw6cyurpvddvzuh48y' then '126'
    when c.validator_to = 'cosmosvaloper1yw5s259jkcg0jzmh7sce29uk0lqqw2ump7578p' then '127'
    when c.validator_to = 'cosmosvaloper1lkujuk2004p3w42tgvuvqnsdmsq8u6jqkwf9wj' then '128'
    when c.validator_to = 'cosmosvaloper140e7u946a2nqqkvcnjpjm83d0ynsqem8dnp684' then '129'
    when c.validator_to = 'cosmosvaloper13x77yexvf6qexfjg9czp6jhpv7vpjdwwkyhe4p' then '130'
    when c.validator_to = 'cosmosvaloper1jxv0u20scum4trha72c7ltfgfqef6nsch7q6cu' then '131'
    when c.validator_to = 'cosmosvaloper1qs8tnw2t8l6amtzvdemnnsq9dzk0ag0z52uzay' then '132'
    when c.validator_to = 'cosmosvaloper1z66j0z75a9flwnez7sa8jxx46cqu4rfhd9q82w' then '133'
    when c.validator_to = 'cosmosvaloper1648ynlpdw7fqa2axt0w2yp3fk542junl7rsvq6' then '134'
    when c.validator_to = 'cosmosvaloper1j0vaeh27t4rll7zhmarwcuq8xtrmvqhudrgcky' then '135'
    when c.validator_to = 'cosmosvaloper1v69lzl909kje64k8vae24uytpxcnpxgullz2dx' then '136'
    when c.validator_to = 'cosmosvaloper103agss48504gkk3la5xcg5kxplaf6ttnuv234h' then '137'
    when c.validator_to = 'cosmosvaloper1sdz4rc95vnzh2f54sacec50vjxnmwdakfym4vh' then '138'
    when c.validator_to = 'cosmosvaloper12lfqufkk2h3w2ycp50czme6nj3ln5tdv7nj3hx' then '139'
    when c.validator_to = 'cosmosvaloper1crqm3598z6qmyn2kkcl9dz7uqs4qdqnr6s8jdn' then '140'
    when c.validator_to = 'cosmosvaloper1ukpah0340rx7k3x2njnavwyjv6pfpvn632df9q' then '141'
    when c.validator_to = 'cosmosvaloper1ualhu3fjgg77g485gmyswkq3w0dp7gys6qzwrv' then '142'
    when c.validator_to = 'cosmosvaloper13ql36flc4cdjhx08hke5vpr4dyv03aafnmvtnc' then '143'
    when c.validator_to = 'cosmosvaloper1urxrvt5dmkqpe50gwrerjly2z6nvk9exjz2j3h' then '144'
    when c.validator_to = 'cosmosvaloper1ff0dw8kawsnxkrgj7p65kvw7jxxakyf8n583gx' then '145'
    when c.validator_to = 'cosmosvaloper1v78emy9d2xe3tj974l7tmn2whca2nh9zp7s0u9' then '146'
    when c.validator_to = 'cosmosvaloper1kyfce0nvluyhgfsdzz8hwrsf5336gsc95pyy4u' then '147'
    when c.validator_to = 'cosmosvaloper1ed5a27kfyu0yljmna00vtr8mgzp6rwh9zn77zz' then '148'
    when c.validator_to = 'cosmosvaloper1usvshtypjw57edkwxq3tagme665398f0hf4wuc' then '149'
    when c.validator_to = 'cosmosvaloper1ha8d55747h8hsaluvz8ld88n24nfaw68rx4x92' then '150'
    when c.validator_to = 'cosmosvaloper1wlpz5hau2ezu0gmuxav63m53d8s77az9wfzlt6' then '151'
    when c.validator_to = 'cosmosvaloper1zc0z44e42qhzltqc8qpj5qrzn836d3lftnqmgw' then '152'
    when c.validator_to = 'cosmosvaloper1rj6324uq904z5zr96zg6ew9qjyau9u6h5nflg6' then '153'
    when c.validator_to = 'cosmosvaloper1yh089p0cre4nhpdqw35uzde5amg3qzexkeggdn' then '154'
    when c.validator_to = 'cosmosvaloper1a4qlael79p76my9pml6thwhnnzsxyy4ajrvd9s' then '155'
    when c.validator_to = 'cosmosvaloper14upntdx8lf0f49t987mj99zksxnluanvu6x4lu' then '156'
    when c.validator_to = 'cosmosvaloper1x3mkgqpshvpq87d33ndsleu7gd7w47dl4ve0yy' then '157'
    when c.validator_to = 'cosmosvaloper10f9wkd6vdspac05djyfwfx0uxcqxapnqhnkcg8' then '158'
    when c.validator_to = 'cosmosvaloper1yfnaup5wa3vdzx3wx9auhvzl85saqj37tqxqnu' then '159'
    when c.validator_to = 'cosmosvaloper1wdrypwex63geqswmcy5qynv4w3z3dyef2qmyna' then '160'
    when c.validator_to = 'cosmosvaloper1de7qx00pz2j6gn9k88ntxxylelkazfk3g8fgh9' then '161'
    when c.validator_to = 'cosmosvaloper1nxe3gnztx8wvayj260dp6yw7jg797m8up02h7z' then '162'
    when c.validator_to = 'cosmosvaloper1u6ddcsjueax884l3tfrs66497c7g86skn7pa0u' then '163'
    when c.validator_to = 'cosmosvaloper1ec3p6a75mqwkv33zt543n6cnxqwun37rr5xlqv' then '164'
    when c.validator_to = 'cosmosvaloper1fun809ksxh87nzf88yashp9ynjz6xkscrtvzvw' then '165'
    when c.validator_to = 'cosmosvaloper1gf3dm2mvqhymts6ksrstlyuu2m8pw6dhfp9md2' then '166'
    when c.validator_to = 'cosmosvaloper15r4tc0m6hc7z8drq3dzlrtcs6rq2q9l2nvwher' then '167'
    when c.validator_to = 'cosmosvaloper1nz3c4q40j8jyvg2hcljkwhe69872mnllf7v9xh' then '168'
    when c.validator_to = 'cosmosvaloper106yp7zw35wftheyyv9f9pe69t8rteumjrx52jg' then '169'
    when c.validator_to = 'cosmosvaloper1v0g7guekttkdmerz5z8hjj8u8j68c6p00zqgf5' then '170'
    when c.validator_to = 'cosmosvaloper12w6tynmjzq4l8zdla3v4x0jt8lt4rcz5gk7zg2' then '171'
    when c.validator_to = 'cosmosvaloper1d0aup392g3enru7eash83sedqclaxvp7fzh6gk' then '172'
    when c.validator_to = 'cosmosvaloper1s05va5d09xlq3et8mapsesqh6r5lqy7mkhwshm' then '173'
    when c.validator_to = 'cosmosvaloper1n3nll7yl3lcv932s2r7l6jzvkjtjk0qppp3rls' then '174'
    else '200' end as to_validator_rank,
    sum(d.amount) as amount_redelegated  from table_9 a 
    left join table_10 b 
    on a.tx_id = b.tx_id 
    left join table_11 c 
    on a.tx_id = c.tx_id
    left join table_12 d
    on a.tx_id = d.tx_id 
    group by from_validator, to_validator, from_validator_rank, to_validator_rank
    
    
    ),
    
    table_0 as (
    select distinct tx_id from cosmos.core.fact_msg_attributes
    where tx_succeeded = 'TRUE'
    and msg_type = 'proposal_vote'
    and attribute_key = 'proposal_id'
    and attribute_value = '82'
    ),
    
    
    -- we keep validators 
      
    table_1 as (select distinct block_timestamp as hourly_date, tx_id, attribute_value as address from cosmos.core.fact_msg_attributes
    where tx_succeeded = 'TRUE'
    and msg_type = 'transfer'
    and attribute_key = 'sender'
    and tx_id in (select * from table_0)
    and attribute_value in ('cosmos1sjllsnramtg3ewxqwwrwjxfgc4n4ef9u0tvx7u',
    'cosmos1c4k24jzduc365kywrsvf5ujz4ya6mwymy8vq4q',
    'cosmos14lultfckehtszvzw4ehu0apvsr77afvyhgqhwh',
    'cosmos1v5y0tg0jllvxf5c3afml8s3awue0ymjuz3aksc',
    'cosmos196ax4vc0lwpxndu9dyhvca7jhxp70rmcfhxsrt',
    'cosmos18ruzecmqj9pv8ac0gvkgryuc7u004te9xr2mcr',
    'cosmos14k4pzckkre6uxxyd2lnhnpp8sngys9m6jtwwnd',
    'cosmos1tflk30mq5vgqjdly92kkhhq3raev2hnzldd74z',
    'cosmos1qaa9zej9a0ge3ugpx3pxyx602lxh3ztqda85ee',
    'cosmos19lss6zgdh5vvcpjhfftdghrpsw7a4434ut4md0',
    'cosmos1ey69r37gfxvxg62sh4r0ktpuc46pzjrmz29g45',
    'cosmos1hjct6q7npsspsg3dgvzk3sdf89spmlpfg8wwf7',
    'cosmos1clpqr4nrk4khgkxj78fcwwh6dl3uw4ep4tgu9q',
    'cosmos156gqf9837u7d4c4678yt3rl4ls9c5vuuxyhkw6',
    'cosmos132juzk0gdmwuxvx4phug7m3ymyatxlh9m9paea',
    'cosmos15urq2dtp9qce4fyc85m6upwm9xul3049um7trd',
    'cosmos1z8zjv3lntpwxua0rtpvgrcwl0nm0tltgyuy0nd',
    'cosmos1vf44d85es37hwl9f4h9gv0e064m0lla62x32sp',
    'cosmos16k579jk6yt2cwmqx9dz5xvq9fug2tekv6g34pl',
    'cosmos1zqgheeawp7cmqk27dgyctd80rd8ryhqsltfszt',
    'cosmos1g48268mu5vfp4wk7dk89r0wdrakm9p5xnm5pr9',
    'cosmos1lzhlnpahvznwfv4jmay2tgaha5kmz5qxuhfk0v',
    'cosmos1gpx52r9h3zeul45amvcy2pysgvcwddxrdjwdll',
    'cosmos1qwl879nx9t6kef4supyazayf7vjhennyjqwjgr',
    'cosmos1gdg6qqe5a3u483unqlqsnullja23g0xv9zj76u',
    'cosmos1n229vhepft6wnkt5tjpwmxdmcnfz55jv5c4tj7',
    'cosmos1ma02nlc7lchu7caufyrrqt4r6v2mpsj92s3mw7',
    'cosmos1vvwtk805lxehwle9l4yudmq6mn0g32pxqjlrmt',
    'cosmos1eh5mwu044gd5ntkkc2xgfg8247mgc56f8pycyz',
    'cosmos1grgelyng2v6v3t8z87wu3sxgt9m5s03xvslewd',
    'cosmos1te8nxpc2myjfrhaty0dnzdhs5ahdh5ag8gswfl',
    'cosmos1rpgtz9pskr5geavkjz02caqmeep7cwwpf29g2p',
    'cosmos14kn0kk33szpwus9nh8n87fjel8djx0y0mmswhp',
    'cosmos1y0us8xvsvfvqkk9c6nt5cfyu5au5tww28lcvjn',
    'cosmos1x88j7vp2xnw3zec8ur3g4waxycyz7m0mcreeaj',
    'cosmos130mdu9a0etmeuw52qfxk73pn0ga6gawkryh2z6',
    'cosmos16fnz0v4cnv5dpnj0p3gaft2q2kzx8z5hvhj0q8',
    'cosmos1we6knm8qartmmh2r0qfpsz6pq0s7emv3um0vsa',
    'cosmos1jst8q8flpn94u9uvkpae8mrkk3a5pjhxrq7swe',
    'cosmos10e4vsut6suau8tk9m6dnrm0slgd6npe3hjqndl',
    'cosmos1kgddca7qj96z0qcxr2c45z73cfl0c75pma99x2',
    'cosmos1cc99d3xcukhedg4wcw53j7a9q68uza70mc4u4d',
    'cosmos19rmlxkqjt950fxl849l49x0me56u9tkd38q8ke',
    'cosmos199mlc7fr6ll5t54w7tts7f4s0cvnqgc5q80f26',
    'cosmos1k2d9ed9vgfuk2m58a2d80q9u6qljkh4vvf589n',
    'cosmos10wljxpl03053h9690apmyeakly3ylhejxgve8g',
    'cosmos1uutuwrwt3z2a5z8z3uasml3rftlpmu25cufp5f',
    'cosmos1ssm0d433seakyak8kcf93yefhknjleed4psy4g',
    'cosmos1ehkfl7palwrh6w2hhr2yfrgrq8jetguceek792',
    'cosmos19yy989ka5usws6gsd8vl94y7l6ssgdwsx8yd7t',
    'cosmos1hjadhj9nqzpye2vkmkz4thahhd0z8dh3eer4jx',
    'cosmos157v7tczs40axfgejp2m43kwuzqe0wsy0xcn5sl',
    'cosmos1gxju9ky3hwxvqqagrl3dxtl49kjpxq6w65d0h8',
    'cosmos1n3mhyp9fvcmuu8l0q8qvjy07x0rql8q4ladl29',
    'cosmos146kwpzhmleafmhtaxulfptyhnvwxzlvmz2rmlg',
    'cosmos1x8efhljzvs52u5xa6m7crcwes7v9u0nlteumau',
    'cosmos14l0fp639yudfl46zauvv8rkzjgd4u0zk0fyvgr',
    'cosmos13nvnv6q8d3yg7tjeahjzljkqu0y27s8yqd2guk',
    'cosmos1dqp325was50l7ut2lnx6s8xhmtwj3wrtrmwaw0',
    'cosmos1lktjhnzkpkz3ehrg8psvmwhafg56kfss5597tg',
    'cosmos1udpsgkgyutgsglauk9vk9rs03a3skc62dg4slh',
    'cosmos10nzaaeh2kq28t3nqsh5m8kmyv90vx7ym304g64',
    'cosmos1sd4tl9aljmmezzudugs7zlaya7pg2895tyn79r',
    'cosmos124maqmcqv8tquy764ktz7cu0gxnzfw54k9cmz5',
    'cosmos1uhnsxv6m83jj3328mhrql7yax3nge5svxcw7kt',
    'cosmos1ptyzewnns2kn37ewtmv6ppsvhdnmeapvwavsg8',
    'cosmos157qezau9xnzypse3vu2vhs7r4ee83fdead6693',
    'cosmos1ul2me6vukg2vac2p6ltxmqlaa7jywdgtz5203m',
    'cosmos17mggn4znyeyg25wd7498qxl7r2jhgue8ep585n',
    'cosmos1q6d3d089hg59x6gcx92uumx70s5y5wadntgvtr',
    'cosmos1sxx9mszve0gaedz5ld7qdkjkfv8z992arw3rr5',
    'cosmos1lcwxu50rvvgf9v6jy6q5mrzyhlszwtjxjlydhj',
    'cosmos1dt93l3qgmhhlp97srjyqyendrgu9nx0sejlm45',
    'cosmos1ej2es5fjztqjcd4pwa0zyvaevtjd2y5wrj4sy7',
    'cosmos1gjtvly9lel6zskvwtvlg5vhwpu9c9wawmyjhz4',
    'cosmos1r2dthxctqzhwg299e7aaeqwfkgcc9hg8n9scjg',
    'cosmos1pjmngrwcsatsuyy8m3qrunaun67sr9x78qhlvr',
    'cosmos10jzj3jjd3frna0ay08sh4zu4fpy957s4qxzrjg',
    'cosmos1m73mgwn3cm2e8x9a9axa0kw8nqz8a4927ywyqq',
    'cosmos1symf474wnypes2d3mecllqk6l26rwz8mvx5csr',
    'cosmos1hdrlqvyjfy5sdrseecjrutyws9khtxxaejwlnd',
    'cosmos17h2x3j7u44qkrq0sk8ul0r2qr440rwgjnau6yy',
    'cosmos1gf4wlkutql95j7wwsxz490s6fahlvk2sqj4m34',
    'cosmos1cgh5ksjwy2sd407lyre4l3uj2fdrqhpk84m04f',
    'cosmos13sduv92y3xdhy3rpmhakrc3v7t37e7psqtmrdl',
    'cosmos1gp957czryfgyvxwn3tfnyy2f0t9g2p4p9ddw25',
    'cosmos1083svrca4t350mphfv9x45wq9asrs60cg0hunp',
    'cosmos1nuhls0wyf8slhmuasha5pz0u89jrf9nneu5j39',
    'cosmos1x8rr4hcf54nz6hfckyy2n05sxss54h8w834fwm',
    'cosmos1thl5syhmscgnj7whdyrydw3w6vy80044jx4x2y',
    'cosmos1keltez56g3zm9w8wr8gcmmulze48g2q3eygmtt',
    'cosmos140l6y2gp3gxvay6qtn70re7z2s0gn57zvenyxp',
    'cosmos1ddle9tczl87gsvmeva3c48nenyng4n56kurw79',
    'cosmos1rwh0cxa72d3yle3r4l8gd7vyphrmjy2kydpnje',
    'cosmos19ecn7ljwp6el2pc5lldyauwv05ufwut9709j08',
    'cosmos1fhr7e04ct0zslmkzqt9smakg3sxrdve6etv27e',
    'cosmos1jlr62guqwrwkdt4m3y00zh2rrsamhjf9kg0p2s',
    'cosmos122j3zmqdl6d2g64qmjuqzj65gfejsvjp22s27q',
    'cosmos1xym2qygmr9vanpa0m7ndk3n0qxgey3ff8vscct',
    'cosmos1e4vye322gkjx8n85jgcclnc7nvdvu82ar8hpnv',
    'cosmos13maqgtlklmereflvg3lq3e8zrp0jsqhrzday69',
    'cosmos1kn3wugetjuy4zetlq6wadchfhvu3x740cdwhk4',
    'cosmos1svwt2mr4x2mx0hcmty0mxsa4rmlfau4ltj72kk',
    'cosmos1wrx0x9m9ykdhw9sg04v7uljme53wuj03cfqce6',
    'cosmos16yupepagywvlk7uhpfchtwa0stu5f8cyjrqq9e',
    'cosmos18extdhzzl5c8tr6453e5hzaj3exrdleaqma8ah',
    'cosmos1e859xaue4k2jzqw20cv6l7p3tmc378pc5znax0',
    'cosmos1rcp29q3hpd246n6qak7jluqep4v006cd4v7r6v',
    'cosmos1vygmh344ldv9qefss9ek7ggsnxparljl7xq0v8',
    'cosmos16s96n9k9zztdgjy8q4qcxp4hn7ww98qkxzfqw9',
    'cosmos1wqy2s6nwnxj57l0l5rdjxxr646p3al6ymmpycg',
    'cosmos1xnrth5rku3z3msm9prxe3l0p2yec3d9m8jks6w',
    'cosmos102ruvpv2srmunfffxavttxnhezln6fnc3pf7tt',
    'cosmos1fsg635n5vgc7jazz9sx5725wnc3xqgr7c6jg3m',
    'cosmos1xwazl8ftks4gn00y5x3c47auquc62ssu9tx6xs',
    'cosmos1e0plfg475phrsvrlzw8gwppeva0zk5ygqauatt',
    'cosmos10unx6s0cdqntvrumd5hs07rgd5ytcztqjnd7zf',
    'cosmos1fqzqejwkk898fcslw4z4eeqjzesynvrdvhqz82',
    'cosmos142w8q2l0gxsfna72gq8t7e4ee4ul37e9jlu724',
    'cosmos1jmykcq8gylmy5tgqtel4xj4q62fdt49s6qnq27',
    'cosmos16qme5yxucnaj6snx35nmwze0wyxr8wfg9jy49a',
    'cosmos1aewyh4gtvayx6v7w592jdfylawk4rsu9wacuyg',
    'cosmos125umsz3fws7gepn5ccsh0sv4gre9r6a3wvvhes',
    'cosmos14qazscc80zgzx3m0m0aa30ths0p9hg8vgut40t',
    'cosmos1et77usu8q2hargvyusl4qzryev8x8t9wt5zn9r',
    'cosmos1485u80fdxjan4sd3esrvyw6cyurpvddv8grqth',
    'cosmos1yw5s259jkcg0jzmh7sce29uk0lqqw2umy2qttj',
    'cosmos1lkujuk2004p3w42tgvuvqnsdmsq8u6jqn6aszp',
    'cosmos140e7u946a2nqqkvcnjpjm83d0ynsqem8g840tx',
    'cosmos13x77yexvf6qexfjg9czp6jhpv7vpjdwwnsrvej',
    'cosmos1jxv0u20scum4trha72c7ltfgfqef6nscj25050',
    'cosmos1qs8tnw2t8l6amtzvdemnnsq9dzk0ag0z37gh3h',
    'cosmos1z66j0z75a9flwnez7sa8jxx46cqu4rfhg35jxa',
    'cosmos1648ynlpdw7fqa2axt0w2yp3fk542junlmhyevf',
    'cosmos1j0vaeh27t4rll7zhmarwcuq8xtrmvqhughud6h',
    'cosmos1v69lzl909kje64k8vae24uytpxcnpxgu6tklp4',
    'cosmos103agss48504gkk3la5xcg5kxplaf6ttnec7yey',
    'cosmos1sdz4rc95vnzh2f54sacec50vjxnmwdakvs0qqy',
    'cosmos12lfqufkk2h3w2ycp50czme6nj3ln5tdvm8xym4',
    'cosmos1crqm3598z6qmyn2kkcl9dz7uqs4qdqnrlyn8pq',
    'cosmos1ukpah0340rx7k3x2njnavwyjv6pfpvn657eufn',
    'cosmos1ualhu3fjgg77g485gmyswkq3w0dp7gysl5km0l',
    'cosmos13ql36flc4cdjhx08hke5vpr4dyv03aafk0c7lt',
    'cosmos1urxrvt5dmkqpe50gwrerjly2z6nvk9exhk78ay',
    'cosmos1ff0dw8kawsnxkrgj7p65kvw7jxxakyf8kqnyy4',
    'cosmos1v78emy9d2xe3tj974l7tmn2whca2nh9zy2y6sk',
    'cosmos1kyfce0nvluyhgfsdzz8hwrsf5336gsc934s3e0',
    'cosmos1ed5a27kfyu0yljmna00vtr8mgzp6rwh9882tw3',
    'cosmos1usvshtypjw57edkwxq3tagme665398f0japmst',
    'cosmos1ha8d55747h8hsaluvz8ld88n24nfaw68xjpnfe',
    'cosmos1wlpz5hau2ezu0gmuxav63m53d8s77az9tak28f',
    'cosmos1zc0z44e42qhzltqc8qpj5qrzn836d3lfw85wya',
    'cosmos1rj6324uq904z5zr96zg6ew9qjyau9u6h38a2yf',
    'cosmos1yh089p0cre4nhpdqw35uzde5amg3qzexnduapq',
    'cosmos1a4qlael79p76my9pml6thwhnnzsxyy4ahhccfr',
    'cosmos14upntdx8lf0f49t987mj99zksxnluanvewjqn0',
    'cosmos1x3mkgqpshvpq87d33ndsleu7gd7w47dlscd6gh',
    'cosmos10f9wkd6vdspac05djyfwfx0uxcqxapnqj8zdy5',
    'cosmos1yfnaup5wa3vdzx3wx9auhvzl85saqj37w5j4l0',
    'cosmos1wdrypwex63geqswmcy5qynv4w3z3dyef0503lw',
    'cosmos1de7qx00pz2j6gn9k88ntxxylelkazfk3dnaamk',
    'cosmos1nxe3gnztx8wvayj260dp6yw7jg797m8uym7zj3',
    'cosmos1u6ddcsjueax884l3tfrs66497c7g86skk24gr0',
    'cosmos1ec3p6a75mqwkv33zt543n6cnxqwun37rxqj2vl',
    'cosmos1fun809ksxh87nzf88yashp9ynjz6xkscxlchqa',
    'cosmos1gf3dm2mvqhymts6ksrstlyuu2m8pw6dhv43wpe',
    'cosmos15r4tc0m6hc7z8drq3dzlrtcs6rq2q9l2kc6z4s',
    'cosmos1nz3c4q40j8jyvg2hcljkwhe69872mnllv2cs2y',
    'cosmos106yp7zw35wftheyyv9f9pe69t8rteumjxjql7m',
    'cosmos1v0g7guekttkdmerz5z8hjj8u8j68c6p02k5a98',
    'cosmos12w6tynmjzq4l8zdla3v4x0jt8lt4rcz5dz2hye',
    'cosmos1d0aup392g3enru7eash83sedqclaxvp7vkr0y9',
    'cosmos1s05va5d09xlq3et8mapsesqh6r5lqy7mnr69mg',
    'cosmos1n3nll7yl3lcv932s2r7l6jzvkjtjk0qpy49knr')),
    
    
    table_2 as (select distinct tx_id, try_parse_json(attribute_value):"option" as voting_option from cosmos.core.fact_msg_attributes
    where tx_succeeded = 'TRUE'
    and msg_type = 'proposal_vote'
    and attribute_key = 'option'
    and tx_id in (select distinct tx_id from table_1)),
    
    table_3 as (
    select max(a.hourly_date) as date , address
      from table_1 a 
    left join table_2 b 
    on a.tx_id = b.tx_id 
    left join osmosis.core.dim_vote_options c 
    on b.voting_option = c.vote_id
    group by address 
    ),
    
    last_table as (
    
      
    select a.tx_id, a.hourly_date,  case when address = 'cosmos1sjllsnramtg3ewxqwwrwjxfgc4n4ef9u0tvx7u' then 'Stake fish '
    when address = 'cosmos1c4k24jzduc365kywrsvf5ujz4ya6mwymy8vq4q' then 'Coinbase Custody'
    when address = 'cosmos14lultfckehtszvzw4ehu0apvsr77afvyhgqhwh' then 'DokiaCapital'
    when address = 'cosmos1v5y0tg0jllvxf5c3afml8s3awue0ymjuz3aksc' then 'Zero Knowledge Validator (ZKV)'
    when address = 'cosmos196ax4vc0lwpxndu9dyhvca7jhxp70rmcfhxsrt' then 'SG-1'
    when address = 'cosmos18ruzecmqj9pv8ac0gvkgryuc7u004te9xr2mcr' then 'Binance node'
    when address = 'cosmos14k4pzckkre6uxxyd2lnhnpp8sngys9m6jtwwnd' then 'Polychain'
    when address = 'cosmos1tflk30mq5vgqjdly92kkhhq3raev2hnzldd74z' then 'Everstake'
    when address = 'cosmos1qaa9zej9a0ge3ugpx3pxyx602lxh3ztqda85ee' then 'Game'
    when address = 'cosmos19lss6zgdh5vvcpjhfftdghrpsw7a4434ut4md0' then 'Paradigm'
    when address = 'cosmos1ey69r37gfxvxg62sh4r0ktpuc46pzjrmz29g45' then 'Sika'
    when address = 'cosmos1hjct6q7npsspsg3dgvzk3sdf89spmlpfg8wwf7' then 'Figment'
    when address = 'cosmos1clpqr4nrk4khgkxj78fcwwh6dl3uw4ep4tgu9q' then 'Cosmostation'
    when address = 'cosmos156gqf9837u7d4c4678yt3rl4ls9c5vuuxyhkw6' then 'Binance staking'
    when address = 'cosmos132juzk0gdmwuxvx4phug7m3ymyatxlh9m9paea' then 'P2P.org'
    when address = 'cosmos15urq2dtp9qce4fyc85m6upwm9xul3049um7trd' then 'Chorus One'
    when address = 'cosmos1z8zjv3lntpwxua0rtpvgrcwl0nm0tltgyuy0nd' then 'Kraken'
    when address = 'cosmos1vf44d85es37hwl9f4h9gv0e064m0lla62x32sp' then 'Multichain ventures'
    when address = 'cosmos16k579jk6yt2cwmqx9dz5xvq9fug2tekv6g34pl' then 'Informal systems'
    when address = 'cosmos1zqgheeawp7cmqk27dgyctd80rd8ryhqsltfszt' then 'No fee to 2025'
    when address = 'cosmos1g48268mu5vfp4wk7dk89r0wdrakm9p5xnm5pr9' then 'Provalidator'
    when address = 'cosmos1lzhlnpahvznwfv4jmay2tgaha5kmz5qxuhfk0v' then 'Citadel.one'
    when address = 'cosmos1gpx52r9h3zeul45amvcy2pysgvcwddxrdjwdll' then 'StakeLab'
    when address = 'cosmos1qwl879nx9t6kef4supyazayf7vjhennyjqwjgr' then 'Certus One'
    when address = 'cosmos1gdg6qqe5a3u483unqlqsnullja23g0xv9zj76u' then 'Zugerselfdelegation'
    when address = 'cosmos1n229vhepft6wnkt5tjpwmxdmcnfz55jv5c4tj7' then 'Allnodes.com'
    when address = 'cosmos1ma02nlc7lchu7caufyrrqt4r6v2mpsj92s3mw7' then 'Hashtower'
    when address = 'cosmos1vvwtk805lxehwle9l4yudmq6mn0g32pxqjlrmt' then 'Imperator.co'
    when address = 'cosmos1eh5mwu044gd5ntkkc2xgfg8247mgc56f8pycyz' then 'Boubounode'
    when address = 'cosmos1grgelyng2v6v3t8z87wu3sxgt9m5s03xvslewd' then 'Inqlusion'
    when address = 'cosmos1te8nxpc2myjfrhaty0dnzdhs5ahdh5ag8gswfl' then 'CoinoneNode'
    when address = 'cosmos1rpgtz9pskr5geavkjz02caqmeep7cwwpf29g2p' then 'Blockpower'
    when address = 'cosmos14kn0kk33szpwus9nh8n87fjel8djx0y0mmswhp' then 'Forbole'
    when address = 'cosmos1y0us8xvsvfvqkk9c6nt5cfyu5au5tww28lcvjn' then 'Swiss Staking'
    when address = 'cosmos1x88j7vp2xnw3zec8ur3g4waxycyz7m0mcreeaj' then 'Staking Facilities'
    when address = 'cosmos130mdu9a0etmeuw52qfxk73pn0ga6gawkryh2z6' then 'strangelove-ventures'
    when address = 'cosmos16fnz0v4cnv5dpnj0p3gaft2q2kzx8z5hvhj0q8' then 'DACM'
    when address = 'cosmos1we6knm8qartmmh2r0qfpsz6pq0s7emv3um0vsa' then 'Staked'
    when address = 'cosmos1jst8q8flpn94u9uvkpae8mrkk3a5pjhxrq7swe' then 'Node Guardians'
    when address = 'cosmos10e4vsut6suau8tk9m6dnrm0slgd6npe3hjqndl' then 'B-Harvest'
    when address = 'cosmos1kgddca7qj96z0qcxr2c45z73cfl0c75pma99x2' then 'ChainLayer'
    when address = 'cosmos1cc99d3xcukhedg4wcw53j7a9q68uza70mc4u4d' then 'dForce'
    when address = 'cosmos19rmlxkqjt950fxl849l49x0me56u9tkd38q8ke' then 'Post Road'
    when address = 'cosmos199mlc7fr6ll5t54w7tts7f4s0cvnqgc5q80f26' then 'ShapeShift DAO'
    when address = 'cosmos1k2d9ed9vgfuk2m58a2d80q9u6qljkh4vvf589n' then 'Stakecito'
    when address = 'cosmos10wljxpl03053h9690apmyeakly3ylhejxgve8g' then 'Ledger'
    when address = 'cosmos1uutuwrwt3z2a5z8z3uasml3rftlpmu25cufp5f' then 'DelegaNetworks '
    when address = 'cosmos1ssm0d433seakyak8kcf93yefhknjleed4psy4g' then 'IRISnet-Bianjie'
    when address = 'cosmos1ehkfl7palwrh6w2hhr2yfrgrq8jetguceek792' then 'KalpaTech'
    when address = 'cosmos19yy989ka5usws6gsd8vl94y7l6ssgdwsx8yd7t' then 'OKEx Pool'
    when address = 'cosmos1hjadhj9nqzpye2vkmkz4thahhd0z8dh3eer4jx' then 'Atomic Nodes'
    when address = 'cosmos157v7tczs40axfgejp2m43kwuzqe0wsy0xcn5sl' then 'POSTHUMAN DVS'
    when address = 'cosmos1gxju9ky3hwxvqqagrl3dxtl49kjpxq6w65d0h8' then 'Vortex.live'
    when address = 'cosmos1n3mhyp9fvcmuu8l0q8qvjy07x0rql8q4ladl29' then '0base.vc'
    when address = 'cosmos146kwpzhmleafmhtaxulfptyhnvwxzlvmz2rmlg' then 'KysenPool Sky'
    when address = 'cosmos1x8efhljzvs52u5xa6m7crcwes7v9u0nlteumau' then 'Upbit Staking'
    when address = 'cosmos14l0fp639yudfl46zauvv8rkzjgd4u0zk0fyvgr' then 'ATEAM'
    when address = 'cosmos13nvnv6q8d3yg7tjeahjzljkqu0y27s8yqd2guk' then 'Latent Iron'
    when address = 'cosmos1dqp325was50l7ut2lnx6s8xhmtwj3wrtrmwaw0' then 'Nocturnal Labs'
    when address = 'cosmos1lktjhnzkpkz3ehrg8psvmwhafg56kfss5597tg' then 'Umbrella '
    when address = 'cosmos1udpsgkgyutgsglauk9vk9rs03a3skc62dg4slh' then 'AUDIT.one'
    when address = 'cosmos10nzaaeh2kq28t3nqsh5m8kmyv90vx7ym304g64' then 'Blockdaemon'
    when address = 'cosmos1sd4tl9aljmmezzudugs7zlaya7pg2895tyn79r' then 'InfStones'
    when address = 'cosmos124maqmcqv8tquy764ktz7cu0gxnzfw54k9cmz5' then 'Simply Staking'
    when address = 'cosmos1uhnsxv6m83jj3328mhrql7yax3nge5svxcw7kt' then 'S16 Research Ventures'
    when address = 'cosmos1ptyzewnns2kn37ewtmv6ppsvhdnmeapvwavsg8' then 'WeStaking'
    when address = 'cosmos157qezau9xnzypse3vu2vhs7r4ee83fdead6693' then 'KuCoin'
    when address = 'cosmos1ul2me6vukg2vac2p6ltxmqlaa7jywdgtz5203m' then 'HyperblocksPro'
    when address = 'cosmos17mggn4znyeyg25wd7498qxl7r2jhgue8ep585n' then '01node'
    when address = 'cosmos1q6d3d089hg59x6gcx92uumx70s5y5wadntgvtr' then 'Ubik Capital 0%Fee'
    when address = 'cosmos1sxx9mszve0gaedz5ld7qdkjkfv8z992arw3rr5' then 'e-Money.com // validator.network'
    when address = 'cosmos1lcwxu50rvvgf9v6jy6q5mrzyhlszwtjxjlydhj' then 'stakezone'
    when address = 'cosmos1dt93l3qgmhhlp97srjyqyendrgu9nx0sejlm45' then '天照☀'
    when address = 'cosmos1ej2es5fjztqjcd4pwa0zyvaevtjd2y5wrj4sy7' then 'Frens '
    when address = 'cosmos1gjtvly9lel6zskvwtvlg5vhwpu9c9wawmyjhz4' then 'EZStaking.io'
    when address = 'cosmos1r2dthxctqzhwg299e7aaeqwfkgcc9hg8n9scjg' then '0% Fee 🌻 Sunflower'
    when address = 'cosmos1pjmngrwcsatsuyy8m3qrunaun67sr9x78qhlvr' then 'Cypher Core'
    when address = 'cosmos10jzj3jjd3frna0ay08sh4zu4fpy957s4qxzrjg' then 'Onbloc Node'
    when address = 'cosmos1m73mgwn3cm2e8x9a9axa0kw8nqz8a4927ywyqq' then '#decentralizehk - DHK dao'
    when address = 'cosmos1symf474wnypes2d3mecllqk6l26rwz8mvx5csr' then 'BlockHunters '
    when address = 'cosmos1hdrlqvyjfy5sdrseecjrutyws9khtxxaejwlnd' then 'SmartNodes'
    when address = 'cosmos17h2x3j7u44qkrq0sk8ul0r2qr440rwgjnau6yy' then 'FreshATOMS.com'
    when address = 'cosmos1gf4wlkutql95j7wwsxz490s6fahlvk2sqj4m34' then 'Stakewolle.com | Auto-compound'
    when address = 'cosmos1cgh5ksjwy2sd407lyre4l3uj2fdrqhpk84m04f' then 'HashQuark'
    when address = 'cosmos13sduv92y3xdhy3rpmhakrc3v7t37e7psqtmrdl' then 'nylira.net'
    when address = 'cosmos1gp957czryfgyvxwn3tfnyy2f0t9g2p4p9ddw25' then 'polkachu.com'
    when address = 'cosmos1083svrca4t350mphfv9x45wq9asrs60cg0hunp' then 'Notional'
    when address = 'cosmos1nuhls0wyf8slhmuasha5pz0u89jrf9nneu5j39' then 'Golden Ratio Staking'
    when address = 'cosmos1x8rr4hcf54nz6hfckyy2n05sxss54h8w834fwm' then 'cosmosgbt'
    when address = 'cosmos1thl5syhmscgnj7whdyrydw3w6vy80044jx4x2y' then 'RockawayX Infra'
    when address = 'cosmos1keltez56g3zm9w8wr8gcmmulze48g2q3eygmtt' then 'DeFi Wallet'
    when address = 'cosmos140l6y2gp3gxvay6qtn70re7z2s0gn57zvenyxp' then 'Lavender.Five Nodes 🐝'
    when address = 'cosmos1ddle9tczl87gsvmeva3c48nenyng4n56kurw79' then 'Witval'
    when address = 'cosmos1rwh0cxa72d3yle3r4l8gd7vyphrmjy2kydpnje' then 'pe4x72'
    when address = 'cosmos19ecn7ljwp6el2pc5lldyauwv05ufwut9709j08' then 'WhisperNode'
    when address = 'cosmos1fhr7e04ct0zslmkzqt9smakg3sxrdve6etv27e' then 'Stakin'
    when address = 'cosmos1jlr62guqwrwkdt4m3y00zh2rrsamhjf9kg0p2s' then 'StakeWithUs'
    when address = 'cosmos122j3zmqdl6d2g64qmjuqzj65gfejsvjp22s27q' then 'COS_Validator'
    when address = 'cosmos1xym2qygmr9vanpa0m7ndk3n0qxgey3ff8vscct' then '🐡grant.fish'
    when address = 'cosmos1e4vye322gkjx8n85jgcclnc7nvdvu82ar8hpnv' then 'Binary Holdings'
    when address = 'cosmos13maqgtlklmereflvg3lq3e8zrp0jsqhrzday69' then 'ChainUp'
    when address = 'cosmos1kn3wugetjuy4zetlq6wadchfhvu3x740cdwhk4' then 'Huobi'
    when address = 'cosmos1svwt2mr4x2mx0hcmty0mxsa4rmlfau4ltj72kk' then 'Twinstake-Validator'
    when address = 'cosmos1wrx0x9m9ykdhw9sg04v7uljme53wuj03cfqce6' then 'Just-Mining'
    when address = 'cosmos16yupepagywvlk7uhpfchtwa0stu5f8cyjrqq9e' then 'Stakely.io'
    when address = 'cosmos18extdhzzl5c8tr6453e5hzaj3exrdleaqma8ah' then 'Smart Stake'
    when address = 'cosmos1e859xaue4k2jzqw20cv6l7p3tmc378pc5znax0' then 'Citizen Cosmos'
    when address = 'cosmos1rcp29q3hpd246n6qak7jluqep4v006cd4v7r6v' then 'in3s.com'
    when address = 'cosmos1vygmh344ldv9qefss9ek7ggsnxparljl7xq0v8' then 'PUPMØS'
    when address = 'cosmos16s96n9k9zztdgjy8q4qcxp4hn7ww98qkxzfqw9' then 'Oni '
    when address = 'cosmos1wqy2s6nwnxj57l0l5rdjxxr646p3al6ymmpycg' then 'Klub Staking'
    when address = 'cosmos1xnrth5rku3z3msm9prxe3l0p2yec3d9m8jks6w' then 'coinhall.org'
    when address = 'cosmos102ruvpv2srmunfffxavttxnhezln6fnc3pf7tt' then 'Ztake.org'
    when address = 'cosmos1fsg635n5vgc7jazz9sx5725wnc3xqgr7c6jg3m' then 'cros-nest'
    when address = 'cosmos1xwazl8ftks4gn00y5x3c47auquc62ssu9tx6xs' then 'jabbey'
    when address = 'cosmos1e0plfg475phrsvrlzw8gwppeva0zk5ygqauatt' then 'Easy 2 Stake'
    when address = 'cosmos10unx6s0cdqntvrumd5hs07rgd5ytcztqjnd7zf' then 'GATA DAO'
    when address = 'cosmos1fqzqejwkk898fcslw4z4eeqjzesynvrdvhqz82' then 'commercio.network'
    when address = 'cosmos142w8q2l0gxsfna72gq8t7e4ee4ul37e9jlu724' then 'NEOPLY'
    when address = 'cosmos1jmykcq8gylmy5tgqtel4xj4q62fdt49s6qnq27' then 'Blocks United | blocksunited.com'
    when address = 'cosmos16qme5yxucnaj6snx35nmwze0wyxr8wfg9jy49a' then 'KIRA Staking'
    when address = 'cosmos1aewyh4gtvayx6v7w592jdfylawk4rsu9wacuyg' then 'Silk Nodes'
    when address = 'cosmos125umsz3fws7gepn5ccsh0sv4gre9r6a3wvvhes' then 'Moonstake'
    when address = 'cosmos14qazscc80zgzx3m0m0aa30ths0p9hg8vgut40t' then 'CryptoCrew Validators ✅'
    when address = 'cosmos1et77usu8q2hargvyusl4qzryev8x8t9wt5zn9r' then 'Stargaze'
    when address = 'cosmos1485u80fdxjan4sd3esrvyw6cyurpvddv8grqth' then 'AIR DROP STATION'
    when address = 'cosmos1yw5s259jkcg0jzmh7sce29uk0lqqw2umy2qttj' then 'CEX.IO'
    when address = 'cosmos1lkujuk2004p3w42tgvuvqnsdmsq8u6jqn6aszp' then 'BitValidator'
    when address = 'cosmos140e7u946a2nqqkvcnjpjm83d0ynsqem8g840tx' then 'danku_zone w/ DAIC'
    when address = 'cosmos13x77yexvf6qexfjg9czp6jhpv7vpjdwwnsrvej' then 'blockscape'
    when address = 'cosmos1jxv0u20scum4trha72c7ltfgfqef6nscj25050' then 'Ping'
    when address = 'cosmos1qs8tnw2t8l6amtzvdemnnsq9dzk0ag0z37gh3h' then 'Castlenode'
    when address = 'cosmos1z66j0z75a9flwnez7sa8jxx46cqu4rfhg35jxa' then 'debo-validator'
    when address = 'cosmos1648ynlpdw7fqa2axt0w2yp3fk542junlmhyevf' then 'Any Labs'
    when address = 'cosmos1j0vaeh27t4rll7zhmarwcuq8xtrmvqhughud6h' then 'Chainflow'
    when address = 'cosmos1v69lzl909kje64k8vae24uytpxcnpxgu6tklp4' then 'Terra Nodes'
    when address = 'cosmos103agss48504gkk3la5xcg5kxplaf6ttnec7yey' then 'MANTRA DAO'
    when address = 'cosmos1sdz4rc95vnzh2f54sacec50vjxnmwdakvs0qqy' then 'Chill Validation'
    when address = 'cosmos12lfqufkk2h3w2ycp50czme6nj3ln5tdvm8xym4' then 'Fanfury | fury.fan | Stake to Win'
    when address = 'cosmos1crqm3598z6qmyn2kkcl9dz7uqs4qdqnrlyn8pq' then 'Coinbase Cloud'
    when address = 'cosmos1ukpah0340rx7k3x2njnavwyjv6pfpvn657eufn' then 'IcyCRO '
    when address = 'cosmos1ualhu3fjgg77g485gmyswkq3w0dp7gysl5km0l' then 'stake.systems'
    when address = 'cosmos13ql36flc4cdjhx08hke5vpr4dyv03aafk0c7lt' then 'TienThuatToan Capital'
    when address = 'cosmos1urxrvt5dmkqpe50gwrerjly2z6nvk9exhk78ay' then 'zoomerlabs'
    when address = 'cosmos1ff0dw8kawsnxkrgj7p65kvw7jxxakyf8kqnyy4' then 'Compass'
    when address = 'cosmos1v78emy9d2xe3tj974l7tmn2whca2nh9zy2y6sk' then 'a41'
    when address = 'cosmos1kyfce0nvluyhgfsdzz8hwrsf5336gsc934s3e0' then 'StakeSeeker by BTCS'
    when address = 'cosmos1ed5a27kfyu0yljmna00vtr8mgzp6rwh9882tw3' then 'CROSSTECH'
    when address = 'cosmos1usvshtypjw57edkwxq3tagme665398f0japmst' then 'Made In Block'
    when address = 'cosmos1ha8d55747h8hsaluvz8ld88n24nfaw68xjpnfe' then 'Lightning Capital'
    when address = 'cosmos1wlpz5hau2ezu0gmuxav63m53d8s77az9tak28f' then '🤑 uGaenn ⛅'
    when address = 'cosmos1zc0z44e42qhzltqc8qpj5qrzn836d3lfw85wya' then 'Virtual Hive'
    when address = 'cosmos1rj6324uq904z5zr96zg6ew9qjyau9u6h38a2yf' then 'Don Cryptonium'
    when address = 'cosmos1yh089p0cre4nhpdqw35uzde5amg3qzexnduapq' then 'High Stakes 🇨🇭'
    when address = 'cosmos1a4qlael79p76my9pml6thwhnnzsxyy4ahhccfr' then 'Multiplex'
    when address = 'cosmos14upntdx8lf0f49t987mj99zksxnluanvewjqn0' then 'Republic Crypto'
    when address = 'cosmos1x3mkgqpshvpq87d33ndsleu7gd7w47dlscd6gh' then 'CrowdControl'
    when address = 'cosmos10f9wkd6vdspac05djyfwfx0uxcqxapnqj8zdy5' then 'Tavis Digital'
    when address = 'cosmos1yfnaup5wa3vdzx3wx9auhvzl85saqj37w5j4l0' then 'Moonlet'
    when address = 'cosmos1wdrypwex63geqswmcy5qynv4w3z3dyef0503lw' then 'Genesis Lab'
    when address = 'cosmos1de7qx00pz2j6gn9k88ntxxylelkazfk3dnaamk' then 'Cosmic Validator | Auto-compound'
    when address = 'cosmos1nxe3gnztx8wvayj260dp6yw7jg797m8uym7zj3' then 'Synclub'
    when address = 'cosmos1u6ddcsjueax884l3tfrs66497c7g86skk24gr0' then 'Sentinel'
    when address = 'cosmos1ec3p6a75mqwkv33zt543n6cnxqwun37rxqj2vl' then 'lunamint'
    when address = 'cosmos1fun809ksxh87nzf88yashp9ynjz6xkscxlchqa' then 'Tessellated'
    when address = 'cosmos1gf3dm2mvqhymts6ksrstlyuu2m8pw6dhv43wpe' then 'Blockapsis'
    when address = 'cosmos15r4tc0m6hc7z8drq3dzlrtcs6rq2q9l2kc6z4s' then 'DragonStake'
    when address = 'cosmos1nz3c4q40j8jyvg2hcljkwhe69872mnllv2cs2y' then 'Interstellar Lounge'
    when address = 'cosmos106yp7zw35wftheyyv9f9pe69t8rteumjxjql7m' then 'Bro_n_Bro'
    when address = 'cosmos1v0g7guekttkdmerz5z8hjj8u8j68c6p02k5a98' then 'LUNC DAO'
    when address = 'cosmos12w6tynmjzq4l8zdla3v4x0jt8lt4rcz5dz2hye' then 'Huobi-1'
    when address = 'cosmos1d0aup392g3enru7eash83sedqclaxvp7vkr0y9' then 'Stir'
    when address = 'cosmos1s05va5d09xlq3et8mapsesqh6r5lqy7mnr69mg' then 'Wetez'
    when address = 'cosmos1n3nll7yl3lcv932s2r7l6jzvkjtjk0qpy49knr' then 'RoundTable21 by WildSage Labs'
    else 'Other' end as label,
    b.voting_option, c.description, count(*) over (partition by label) as num_votes from table_1 a 
    left join table_2 b 
    on a.tx_id = b.tx_id 
    left join osmosis.core.dim_vote_options c 
    on b.voting_option = c.vote_id
    where (a.hourly_date, address) in (select * from table_3)
    
    ),
    
    PROPOSAL_82_VALIDATOR_VOTES AS (
    
    select DISTINCT  label,  
    case when label = 'Cosmostation' then 4 else voting_option end as voting_option, case  when label = 'Cosmostation' THEN 'NO WITH VETO' ELSE DESCRIPTION END AS DESCRIPTION FROM LAST_TABLE 
    ),
    
    last_table_2 as (
    select from_validator, to_validator, from_validator_rank, to_validator_rank,
    case when b.voting_option is null then 5 else b.voting_option end as from_voting_option, 
    case when b.description is null then 'DID NOT VOTE' else b.description end as from_vote, 
    case when c.voting_option is null then 5 else c.voting_option end as to_voting_option,
    case when c.description is null then 'DID NOT VOTE' else c.description end as to_vote,  
      amount_redelegated  from sankey_data a 
    left join PROPOSAL_82_VALIDATOR_VOTES b 
    on a.from_validator = b.label 
    left join PROPOSAL_82_VALIDATOR_VOTES c
    on a.to_validator = c.label )
       
    select from_vote as from_validator, from_voting_option as from_validator_rank, to_vote as to_validator, to_voting_option as to_validator_rank, sum(amount_redelegated) as amount_redelegated from last_table_2 
      where from_vote != to_vote
      group by from_vote, from_voting_option, to_vote, to_voting_option
    
    	  
    	"""  
    	 
    
    TTL_MINUTES = 15
    # return up to 100,000 results per GET request on the query id
    PAGE_SIZE = 100000
    # return results of page 1
    PAGE_NUMBER = 1
     
    def create_query_3():
    	r = requests.post(
    			'https://node-api.flipsidecrypto.com/queries',  
    			data=json.dumps({
    				"sql": SQL_QUERY_3,
    				"ttlMinutes": TTL_MINUTES
    			}),
    			headers={"Accept": "application/json", "Content-Type": "application/json", "x-api-key": API_KEY},
    	)
    	if r.status_code != 200:
    		raise Exception("Error creating query, got response: " + r.text + "with status code: " + str(r.status_code))
    		
    	return json.loads(r.text)    
    	 
    
     
    
    def get_query_results_3(token):
    	r = requests.get(
    			'https://node-api.flipsidecrypto.com/queries/{token}?pageNumber={page_number}&pageSize={page_size}'.format(
    			  token=token,
    			  page_number=PAGE_NUMBER,
    			  page_size=PAGE_SIZE
    			),
    			headers={"Accept": "application/json", "Content-Type": "application/json", "x-api-key": API_KEY}
    	)
    	if r.status_code != 200:
    		raise Exception("Error getting query results, got response: " + r.text + "with status code: " + str(r.status_code))
    		
    	data = json.loads(r.text)
    	if data['status'] == 'running':
    		time.sleep(10)
    		return get_query_results_3(token)
    
    	return data
    
    
    query_3 = create_query_3()
    token_3 = query_3.get('token')
    data3 = get_query_results_3(token_3) 
    df5 = pd.DataFrame(data3['results'], columns = ['FROM_VALIDATOR', 'FROM_VALIDATOR_RANK','TO_VALIDATOR','TO_VALIDATOR_RANK','AMOUNT_REDELEGATED'])
    
    
    	  
     
    list11 = ['1','2','3','4','5']
    list22 = ['YES','ABSTAIN','NO','NO WITH VETO','DID NOT VOTE']
    list33 = [1, 2, 3, 4, 5]
    df6 = pd.DataFrame()
    
    df6['ADDRESS'] = list11
    
    df6['LABEL'] = list22
    
    df6['RANK'] = list33
    
    randcolor = []
    
    for i in range(1,len(df6['LABEL']) + 1):
    	 
    	randcolor.append("#{:06x}".format(random.randint(0, 0xFFFFFF))) 
    		
    df6['COLOR'] = randcolor
    
    
    keys_list_2 =  df6['RANK']
    values_list_2 = df6['LABEL']
    zip_iterator_2 = zip(keys_list_2, values_list_2) 
    a_dictionary_2 = dict(zip_iterator_2)
    
    
    
    df7 = pd.DataFrame(a_dictionary_2.items(), columns = ['RANK','LABEL'], index = keys_list_2)
    df7.index = df7.index
    df7 = df7.sort_index()
    
    
    
    df5['FROM_VALIDATOR_RANK'] = df5['FROM_VALIDATOR_RANK'].astype('int')
    df5['TO_VALIDATOR_RANK'] = df5['TO_VALIDATOR_RANK'].astype('int')

    	
    validator_choice_2 = st.selectbox("Choose a validator", options = df5['FROM_VALIDATOR'].unique() )
    
    		
    df_filtered_2 = df5[df5['FROM_VALIDATOR'] == validator_choice_2]
    df_filtered_2['Link color'] = 'rgba(127, 194, 65, 0.2)'
    df_filtered_2['FROM_VALIDATOR_RANK'] = df_filtered_2['FROM_VALIDATOR_RANK']-1
    df_filtered_2['TO_VALIDATOR_RANK'] = df_filtered_2['TO_VALIDATOR_RANK'] - 1
    
    link_1 = dict(source = df_filtered_2['FROM_VALIDATOR_RANK'].values , target = df_filtered_2['TO_VALIDATOR_RANK'].values, value = df_filtered_2['AMOUNT_REDELEGATED'], color = df6['COLOR'])
    node_1 = dict(label = df7['LABEL'].values, pad = 35, thickness = 10)
    
    	 
    		
    		 
    data = go.Sankey(link = link_1, node = node_1)
    fig = go.Figure(data)
    fig.update_layout(
    			hovermode = 'x', 
    			font = dict(size = 20, color = 'white'), 
    			paper_bgcolor= 'rgba(0,0,0,0)',
    			width=1000, height=1300
    ) 
    		
    st.plotly_chart(fig, use_container_width=True) 
    
    
    


