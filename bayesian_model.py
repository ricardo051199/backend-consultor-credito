from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

modelo = BayesianModel([('Pb', 'Hp'), ('Em', 'Hp'), ('Hp','C'), ('Em','C'), ('Bi', 'Mb'), ('Bi', 'Bif'), ('Mb', 'Bif'), ('Pb', 'Dc'), ('C', 'Dc'), ('Bif', 'Dc')])

cpd_em = TabularCPD(variable='Em', variable_card=2, values=[[0.65], [0.35]])
cpd_bi = TabularCPD(variable='Bi', variable_card=2, values=[[0.56], [0.44]])
cpd_pb = TabularCPD(variable='Pb', variable_card=2, values=[[0.78], [0.22]])
cpd_hp = TabularCPD(variable='Hp', variable_card=2, values=[[0.78, 0.64, 0.66, 0.2], [0.22, 0.36, 0.34, 0.8]],
                    evidence=['Em', 'Pb'], evidence_card=[2, 2])
cpd_bif = TabularCPD(variable='Bif', variable_card=2, values=[[0.88, 0.51, 0.62, 0.35], [0.12, 0.49, 0.38, 0.65]],
                     evidence=['Mb', 'Bi'], evidence_card=[2, 2])
cpd_c = TabularCPD(variable='C', variable_card=2, values=[[0.88, 0.58, 0.69, 0.12], [0.12, 0.42, 0.31, 0.88]],
                   evidence=['Em', 'Hp'], evidence_card=[2, 2])
cpd_mb = TabularCPD(variable='Mb', variable_card=2, values=[[0.86, 0.34], [0.14, 0.66]], evidence=['Bi'], evidence_card=[2])
cpd_dc = TabularCPD(variable='Dc', variable_card=2, values=[[0.98, 0.78, 0.73, 0.23, 0.82, 0.2, 0.23, 0],
                                                             [0.02, 0.22, 0.27, 0.77, 0.18, 0.8, 0.77, 1]],
                    evidence=['Pb', 'C', 'Bif'], evidence_card=[2, 2, 2])

modelo.add_cpds(cpd_pb, cpd_em, cpd_bi, cpd_hp, cpd
