import pandas as pd
import numpy as np

def prettyPrintCVScores(cv_metric):
    '''
    Generic pretty printer of a cross validation
    '''
    print('CV Results')
    print('='*32)
    print('Accuracy')
    print('-'*32)
    print(f"Training accuracy: {cv_metric['train_accuracy'].mean():.3f}")
    print(f"Test accuracy:     {cv_metric['test_accuracy'].mean():.3f}")
    print('F-1 Score')
    print('-'*32)
    print(f"Training F1 score: {cv_metric['train_f1_macro'].mean():.3f}")
    print(f"Test F1 score:     {cv_metric['test_f1_macro'].mean():.3f}")
    
    
    
def prettyPrintGridCVResults(GSCVModel):
    '''
    Tabulates results a grid search.
    Ranks by accuracy
    Shows all 4 mean test metrics: Accuracy, Precision Macro, Recall Macro, F1-score Macro
    Shows all parameters used for that model
    '''
    
    list_cols = ['rank_test_accuracy']
    list_metrics = ['mean_test_accuracy', 'mean_test_precision_macro',
                      'mean_test_recall_macro', 'mean_test_f1_macro']
    list_cols.extend(list_metrics)

    for col in GSCVModel.cv_results_.keys():
        if col.startswith('param_'):
            list_cols.append(col)
    
    


    table = pd.DataFrame(GSCVModel.cv_results_)
    for m in list_metrics:
        table[m] = table[m].map('{:,.4f}'.format)
    table = table[list_cols].sort_values(by='rank_test_accuracy')
    

        
    table.rename(columns={'rank_test_accuracy': 'Rank (By Accuracy)',
                          'mean_test_accuracy': 'Mean Test Accuracy',
                          'mean_test_precision_macro': 'Mean Test Precision (macro)',
                          'mean_test_recall_macro': 'Mean Test Recall (macro)',
                          'mean_test_f1_macro': 'Mean Test F1-Score (macro)'
                          }, inplace=True)
    

    return table.set_index('Rank (By Accuracy)')
