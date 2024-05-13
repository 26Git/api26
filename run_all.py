import logging
import pickle,sys
import unittest
from lib.HTMLTestRunner import HTMLTestRunner
from lib.send_email import send_email
from config.config import *
from test.suit.test_suit import *
import time

# class MyTestCase(unittest.TestCase):
#     def test_all(self):
#         logging.info("================运行所有的case================")
#         suit=unittest.defaultTestLoader.discover(test_path,'test*.py')
#         # t = time.strftime('%Y_%m_%d_%H_%M_%S')
#         with open(report_file,'wb')as f:
#             HTMLTestRunner(
#                 stream=f,
#                 title='xzs测试用例',
#                 description='xzs登陆和注册用例集',
#                 verbosity=2
#             ).run(suit)
#
#         send_email(report_file)
#         logging.info("================测试结束================")
#
# if __name__ == '__main__':
#     unittest.main()

def discoyer():
    return unittest.defaultTestLoader.discover(test_case_path)
def run(suite):
    logging.info("====测试开始====")
    with open(report_file,'wb') as f:
        result = HTMLTestRunner(stream=f,
                       title="接口测试",
                       description="测试描述",
                       verbosity=2
                       ).run(suite)
    if result.failures:
        save_failures(result,last_fails_file)
        logging.error("测试失败，失败用例已保存到文件：{}".format(last_fails_file))
    else:
        logging.info("测试成功")
    if send_email_after_run:
        send_email(report_file)
    send_email(report_file)
    logging.info("====测试结束====")
def run_all():
    run(discoyer())
def run_suite(suite_name):
    suite = get_suit(suite_name)
    print(suite)
    if isinstance(suite,unittest.TestSuite):
        run(suite)
    else:
        print("TestSuite不存在")

def collect():
    suite = unittest.TestSuite()
    def _collect(tests):
        if isinstance(tests,unittest.TestSuite): # 如果下级元素还是TestSuite则继续往下找
            if tests.countTestCases() != 0:# 如果TestSuite中有用例则继续往下找
                for i in tests:# 遍历TestSuite
                    _collect(i)# 递归调用
        else:
            suite.addTest(tests)# 如果下级元素是TestCase，则添加到TestSuite中
    _collect(discoyer())# unittest.defaultTestLoader.discover(tset_case_path)
    return suite
def collect_only():#仅列出所用用例
    t0 = time.time()#开始时间
    i = 0# 用例计数
    for case in collect():# 遍历TestSuite
        i += 1# 计数加1
        print("{}.{}".format(str(i),case.id()))# 输出用例名称
    print("-------------------------------------------------")
    print("Collect {} tests is {:.3f}s".format(str(i), time.time() - t0))# 输出用例总数和用时

def makesuit_by_testlist(test_list_file):
    with open(test_list_file,encoding='utf-8') as f:
        testlist = f.readlines()

        # 去掉每行结尾的“/n”和#号开头的行
        testlist = [i.strip() for i in testlist if not i.startswith("#")]
        print(testlist)
        suite = unittest.TestSuite()
        all_cases = collect()#获取工程test/case目录以及子目录下所有Test'Case'
        for case in all_cases:
            case_name = case.id().split('.')[-1]
            if case_name in testlist:
                suite.addTest(case)
        return suite

# 根据tag来组建suite
def makesuite_by_tag(tag):
    # 申明一个suite
    suite = unittest.TestSuite()
    # 获取当前所有的testcase
    for i in collect():
        # tag和标签都包含的时候
        if i._testMethodDoc and tag in i._testMethodDoc:
            # 添加到suite中
            suite.addTest(i)
        return suite

def save_failures(result,file):
    suite = unittest.TestSuite()
    for case_result in result.failures:
        suite.addTest(case_result[0])
    with open(file,'wb') as f:
        pickle.dump(suite,f)

def rerun_fails():
    sys.path.append(test_case_path)
    with open(last_fails_file,'rb') as f:
        suite = pickle.load(f)
    run(suite)

def main():
    if options.collect_only:
        collect_only()
    elif options.rerun_fails:
        rerun_fails()
    elif options.tag:
        run(makesuite_by_tag(options.tag))
    else:
        run_all()

if __name__ == '__main__':
    # suite = makesuit_by_testlist(test_list_file)
    # suite = makesuite_by_tag("level1")
    # run(suite)
    # rerun_fails()
    # run_all()
    main()