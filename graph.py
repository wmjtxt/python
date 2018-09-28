# -*- coding: UTF-8 -*-

"""
Created on 17-11-28

@summary: ʵ�ִ�ͳ��ǩ�����㷨LPA

@author: dreamhome

"""

import random
import networkx as nx
import matplotlib.pyplot as plt


def read_graph_from_file(path):
    """
    :param path: ���ļ��ж�ȡͼ�ṹ
    :return: Graph graph
    """
    # ����ͼ
    graph = nx.Graph()
    # ��ȡ���б�edges_list
    edges_list = []
    # ��ʼ��ȡ��
    fp = open(path)
    edge = fp.readline().split()
    while edge:
        if edge[0].isdigit() and edge[1].isdigit():
            edges_list.append((int(edge[0]), int(edge[1])))
        edge = fp.readline().split()
    fp.close()
    # Ϊͼ���ӱ�
    graph.add_edges_from(edges_list)

    # ��ÿ���ڵ����ӱ�ǩ
    for node, data in graph.nodes_iter(True):
        data['label'] = node

    return graph


def lpa(graph):
    """
    ��ǩ�����㷨 ʹ���첽���·�ʽ
    :param graph:
    :return:
    """
    def estimate_stop_condition():
        """
        �㷨��ֹ���������нڵ�ı�ǩ��󲿷��ھӽڵ��ǩ��ͬ���ߵ�����������ָ��ֵ��ֹͣ
        :return:
        """
        for node in graph.nodes_iter():
            count = {}
            for neighbor in graph.neighbors_iter(node):
                neighbor_label = graph.node[neighbor]['label']
                count[neighbor_label] = count.setdefault(
                    neighbor_label, 0) + 1

            # �ҵ�����ֵ����label
            count_items = count.items()
            count_items.sort(key=lambda x: x[1], reverse=True)
            labels = [k for k, v in count_items if v == count_items[0][1]]
            # ���ڵ��ǩ��󲿷��ھӽڵ��ǩ��ͬʱ��ﵽֹͣ����
            if graph.node[node]['label'] not in labels:
                return False

        return True

    loop_count = 0

    # ������ǩ��������
    while True:
        loop_count += 1
        print('��������', loop_count)

        for node in graph.nodes_iter():
            count = {}
            for neighbor in graph.neighbors_iter(node):
                neighbor_label = graph.node[neighbor]['label']
                count[neighbor_label] = count.setdefault(
                    neighbor_label, 0) + 1

            # �ҵ�����ֵ���ı�ǩ
            count_items = count.items()
            # print count_items
            count_items.sort(key=lambda x: x[1], reverse=True)
            labels = [(k, v) for k, v in count_items if v == count_items[0][1]]
            # �������ǩ������ֵ��ͬʱ���ѡȡһ����ǩ
            label = random.sample(labels, 1)[0][0]
            graph.node[node]['label'] = label

        if estimate_stop_condition() is True or loop_count >= 10:
            print('complete')
            return


if __name__ == "__main__":

    path = "E:\\2018\\工程实践报告\\data\\dolphins.csv"
    graph = read_graph_from_file(path)
    lpa(graph)

    # �����㷨�����ͼ
    node_color = [float(graph.node[v]['label']) for v in graph]
    nx.draw_networkx(graph, node_color=node_color)
    plt.show()