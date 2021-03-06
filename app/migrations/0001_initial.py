# Generated by Django 2.1.5 on 2019-01-16 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget_result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sum_carriage', models.CharField(max_length=20, verbose_name='总运费收入')),
                ('Profit_loss', models.CharField(max_length=20, verbose_name='利润/亏损 ')),
                ('Rent_level', models.CharField(max_length=20, verbose_name='相当租金水平')),
                ('Huikou_commission_p', models.CharField(max_length=20, verbose_name='回扣佣金')),
                ('Agent_commission_p', models.CharField(max_length=20, verbose_name='经纪人佣金')),
            ],
            options={
                'verbose_name': '预算结果',
                'verbose_name_plural': '预算结果',
            },
        ),
        migrations.CreateModel(
            name='Cost_result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sum_fuel', models.CharField(max_length=20, verbose_name='燃油费')),
                ('Sum_Pport_cost', models.CharField(max_length=20, verbose_name='总港口费用')),
                ('Sum_day_rent', models.CharField(max_length=20, verbose_name='总船舶租金（净）')),
                ('Sum_Cost', models.CharField(max_length=20, verbose_name='总成本')),
                ('Day_cost', models.CharField(max_length=20, verbose_name='每日成本')),
            ],
            options={
                'verbose_name': '成本预算结果',
                'verbose_name_plural': '成本预算结果',
            },
        ),
        migrations.CreateModel(
            name='Fuel_rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FO_sea', models.CharField(max_length=20, verbose_name='FO在航消耗油量')),
                ('FO_port', models.CharField(max_length=20, verbose_name='FO在港消耗油量')),
                ('FO_price', models.CharField(max_length=20, verbose_name='FO油价')),
                ('DO_sea', models.CharField(max_length=20, verbose_name='DO在航消耗油量')),
                ('DO_port', models.CharField(max_length=20, verbose_name='DO在港消耗油量')),
                ('DO_price', models.CharField(max_length=20, verbose_name='DO油价')),
                ('FO', models.CharField(max_length=20, verbose_name='fO价格参考')),
                ('DO', models.CharField(max_length=20, verbose_name='DO价格参考')),
                ('Day_rent', models.CharField(max_length=20, verbose_name='日租金')),
                ('Commission', models.CharField(max_length=20, verbose_name='佣金')),
            ],
            options={
                'verbose_name': '燃烧费及租金',
                'verbose_name_plural': '燃烧费及租金',
            },
        ),
        migrations.CreateModel(
            name='Pcargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pcargo_name', models.CharField(max_length=30, verbose_name='货物名')),
                ('Pcargo_num', models.CharField(max_length=20, verbose_name='货物量')),
                ('Pcargo_carriage', models.CharField(max_length=20, verbose_name='运费')),
                ('Huikou_commission_p', models.CharField(max_length=20, verbose_name='回扣佣金')),
                ('Agent_commission_p', models.CharField(max_length=20, verbose_name='代理人佣金 ')),
                ('Carriage_tax', models.CharField(max_length=20, verbose_name='运费税')),
                ('Item_tax', models.CharField(max_length=20, verbose_name='其他扣除项')),
                ('Carriage_revenue', models.CharField(max_length=20, verbose_name='运费收益')),
            ],
            options={
                'verbose_name': '运费收益',
                'verbose_name_plural': '运费收益',
            },
        ),
        migrations.CreateModel(
            name='Pport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pport_order', models.IntegerField(verbose_name='顺序编号')),
                ('Pport_name', models.CharField(max_length=50, verbose_name='港口名')),
                ('Pport_shipstate', models.CharField(choices=[('0', '装货'), ('1', '卸货'), ('3', '加油')], max_length=100, verbose_name='船舶状态')),
                ('Pport_leisureday', models.IntegerField(verbose_name='空闲天数')),
                ('Pport_workday', models.IntegerField(verbose_name='工作天数')),
                ('Pport_eta', models.DateTimeField(max_length=20, verbose_name='ETA')),
                ('Pport_etd', models.DateTimeField(max_length=20, verbose_name='ETD')),
                ('Pport_cost', models.IntegerField(verbose_name='港口费用')),
                ('Pport_range', models.IntegerField(blank=True, null=True, verbose_name='航程距离')),
                ('Pport_shipday', models.IntegerField(blank=True, null=True, verbose_name='在航天数')),
            ],
            options={
                'verbose_name': '港口信息',
                'verbose_name_plural': '港口信息',
                'ordering': ['Pport_name'],
            },
        ),
        migrations.CreateModel(
            name='Pship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pship_number', models.CharField(max_length=200, unique=True, verbose_name='航次')),
                ('Pship_name', models.CharField(max_length=20, verbose_name='船舶名')),
                ('Pship_load', models.FloatField(verbose_name='载重吨')),
                ('Pship_hovel', models.FloatField(verbose_name='舱容')),
                ('Pship_speed', models.FloatField(blank=True, default=12, null=True, verbose_name='默认航速')),
            ],
            options={
                'verbose_name': '船舶信息',
                'verbose_name_plural': '船舶信息',
            },
        ),
        migrations.CreateModel(
            name='Pship_Pport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pport_order', models.CharField(max_length=20, verbose_name='经过港口顺序')),
                ('Sum_range', models.IntegerField(verbose_name='总航行距离')),
                ('Sum_day', models.IntegerField(verbose_name='总航行时间')),
                ('Pport_lei_worday', models.IntegerField(verbose_name='总在港时间')),
                ('Pport_range', models.IntegerField(verbose_name='总在航时间')),
                ('Start_day', models.CharField(max_length=50, verbose_name='开始时间')),
                ('End_day', models.CharField(max_length=50, verbose_name='结束时间')),
                ('Pship_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pship')),
            ],
            options={
                'verbose_name': '计算航程信息',
                'verbose_name_plural': '计算航程信息',
            },
        ),
        migrations.AddField(
            model_name='pport',
            name='Pship_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pship'),
        ),
        migrations.AddField(
            model_name='pcargo',
            name='Pship_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pship'),
        ),
        migrations.AddField(
            model_name='fuel_rent',
            name='Pship_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pship'),
        ),
        migrations.AddField(
            model_name='cost_result',
            name='Pship_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pship'),
        ),
        migrations.AddField(
            model_name='budget_result',
            name='Pship_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pship'),
        ),
    ]
